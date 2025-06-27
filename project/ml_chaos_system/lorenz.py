import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks, welch
from mpl_toolkits.mplot3d import Axes3D


# --------- 1. Generate Lorenz system data ---------

def lorenz(t, state, sigma=10.0, beta=8/3, rho=28.0):
    x, y, z = state
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)
dt = t_eval[1] - t_eval[0] # time step as 0.01 

state0 = [1.0, 1.0, 1.0]
sol = solve_ivp(lorenz, t_span, state0, t_eval=t_eval)
data = sol.y.T # transpose to shape (10000, 3) since sol.y has 3 variables, 10000 time steps
print(f"Generated Lorenz data shape: {data.shape}")

# --------- 2. Reservoir creation ---------

# A is the internal recurrent matrix
# 
def create_reservoir(input_dim, reservoir_size, spectral_radius, input_scaling=0.1, sparsity=0.012):
    A = np.random.rand(reservoir_size, reservoir_size) - 0.5
    mask = np.random.rand(*A.shape) < sparsity
    A *= mask
    eigvals = np.abs(np.linalg.eigvals(A))
    A /= np.max(eigvals)
    A *= spectral_radius

    Win = (np.random.rand(reservoir_size, input_dim) - 0.5) * input_scaling
    return A, Win

def train_reservoir(A, Win, data, lambda_reg=1e-3, washout=500):
    reservoir_size = A.shape[0]
    r = np.zeros(reservoir_size)
    R_collect, U_collect = [], []

    for u in data:
        r_input = A @ r + Win @ u
        r_input = np.clip(r_input, -50, 50)
        r = np.tanh(r_input)
        R_collect.append(r.copy())
        U_collect.append(u.copy())

    R_collect = np.stack(R_collect)
    U_collect = np.stack(U_collect)

    R_train = R_collect[washout:]
    U_train = U_collect[washout:]
    Wout = np.linalg.solve(R_train.T @ R_train + lambda_reg*np.eye(reservoir_size), R_train.T @ U_train)
    return Wout, r

def predict(A, Win, Wout, r0, steps):
    r_pred = r0.copy()
    predictions = []

    for _ in range(steps):
        u_pred = Wout.T @ r_pred
        r_input = A @ r_pred + Win @ u_pred
        r_input = np.clip(r_input, -50, 50)
        r_pred = np.tanh(r_input)
        predictions.append(u_pred)

    return np.stack(predictions)

def compute_lyapunov_exponents(A, Win, Wout, r0, num_exponents=3, steps=5000, dt=1.0):
    Dr = A.shape[0]
    r = np.copy(r0)

    perturbations = np.random.randn(Dr, num_exponents)
    q, _ = np.linalg.qr(perturbations)
    perturbations = q

    lyapunov_sums = np.zeros(num_exponents)

    for step in range(steps):
        input_effect = Win @ (Wout.T @ r)
        r_input = A @ r + input_effect
        r_input = np.clip(r_input, -50, 50)
        r = np.tanh(r_input)

        diag = 1 - r**2
        J = np.diag(diag) @ (A + Win @ Wout.T)

        perturbations = J @ perturbations
        q, rmat = np.linalg.qr(perturbations)
        perturbations = q

        lyapunov_sums += np.log(np.abs(np.diag(rmat)) + 1e-10)

    return lyapunov_sums / (steps * dt)

# --------- 3. Train reservoir ---------

reservoir_size = 500
input_dim = 3
spectral_radius = 1.2
input_scaling = 0.1
sparsity = 6 / 500  # average degree ~6

A, Win = create_reservoir(input_dim, reservoir_size, spectral_radius, input_scaling, sparsity)
Wout, _ = train_reservoir(A, Win, data)

# --------- 4. Autonomous prediction (reset r0!) ---------

r0_pred = np.random.uniform(-0.1, 0.1, size=(reservoir_size,))
predictions = predict(A, Win, Wout, r0_pred, steps=len(data))

# --------- 5. Plotting: x(t), y(t), z(t) ---------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(data[:,0], data[:,1], data[:,2], lw=0.5)
ax.set_xlabel('x'), ax.set_ylabel('y'), ax.set_zlabel('z')
plt.title('Lorenz Attractor')
plt.show()
fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

axs[0].plot(t_eval, data[:, 0], label="True x", alpha=0.7)
axs[0].plot(t_eval, predictions[:, 0], '--', label="Predicted x")
axs[0].set_ylabel("x")
axs[0].legend()
axs[0].grid()

axs[1].plot(t_eval, data[:, 1], label="True y", alpha=0.7)
axs[1].plot(t_eval, predictions[:, 1], '--', label="Predicted y")
axs[1].set_ylabel("y")
axs[1].legend()
axs[1].grid()

axs[2].plot(t_eval, data[:, 2], label="True z", alpha=0.7)
axs[2].plot(t_eval, predictions[:, 2], '--', label="Predicted z")
axs[2].set_ylabel("z")
axs[2].set_xlabel("Time")
axs[2].legend()
axs[2].grid()

plt.suptitle("Lorenz System: True vs Predicted")
plt.tight_layout()
plt.show()

# --------- 6. Return map of z maxima ---------

def plot_return_map(true_z, pred_z, title):
    peaks_true, _ = find_peaks(true_z)
    peaks_pred, _ = find_peaks(pred_z)

    z_max_true = true_z[peaks_true]
    z_max_pred = pred_z[peaks_pred]

    plt.figure(figsize=(8, 6))
    plt.plot(z_max_true[:-1], z_max_true[1:], 'bo', label='True Lorenz')
    plt.plot(z_max_pred[:-1], z_max_pred[1:], 'r.', label='Reservoir Prediction')
    plt.xlabel(r"$z_i$")
    plt.ylabel(r"$z_{i+1}$")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

plot_return_map(data[:,2], predictions[:,2], "Return Map")


# --------- 7. Compute Lyapunov exponents ---------

lyap = compute_lyapunov_exponents(A, Win, Wout, np.random.uniform(-0.1, 0.1, size=(reservoir_size,)), steps=5000, dt=dt)
print("Lyapunov exponents:", lyap)
