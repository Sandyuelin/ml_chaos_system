import numpy as np
import matplotlib.pyplot as plt

# Time step and total steps
dt = 0.01
num_steps = 10000

# Initialize arrays
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Initial conditions
xs[0], ys[0], zs[0] = (0.1, 1.0, 1.05)

# Lorenz system parameters
s = 10.0
r = 28.0
b = 2.667

# Euler integration
for i in range(num_steps):
    dx = s * (ys[i] - xs[i])
    dy = xs[i] * (r - zs[i]) - ys[i]
    dz = xs[i] * ys[i] - b * zs[i]
    
    xs[i+1] = xs[i] + dx * dt
    ys[i+1] = ys[i] + dy * dt
    zs[i+1] = zs[i] + dz * dt

# Time vector
t = np.linspace(0, dt*num_steps, num_steps+1)

# Plot each variable in its own subplot
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

axes[0].plot(t, xs, color='C0')
axes[0].set_ylabel('x(t)')
axes[0].grid(True)

axes[1].plot(t, ys, color='C1')
axes[1].set_ylabel('y(t)')
axes[1].grid(True)

axes[2].plot(t, zs, color='C2')
axes[2].set_ylabel('z(t)')
axes[2].set_xlabel('Time')
axes[2].grid(True)

plt.suptitle('Lorenz System via Euler Method')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
