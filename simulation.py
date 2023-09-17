import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Half-pipe parameters
H = 7
W = 20
L = 180
a = H / (W/2)**2

# Generate half-pipe
X = np.linspace(0, L, 400)
Y = np.linspace(-W/2, W/2, 400)
X, Y = np.meshgrid(X, Y)
Z = a * Y**2

# Adjust Z to ensure it starts from a positive elevation and ends at ground level
elevation_adjustment = L * np.tan(np.deg2rad(18))
Z = Z - X * np.tan(np.deg2rad(18)) + elevation_adjustment

# Simulate snowboarder's motion
g = 9.81  # m/s^2
angle = np.deg2rad(18)
g_slope = g * np.sin(angle)
dt = 0.01  # time step

x_snowboarder = 0  # starting at the left end
y_snowboarder = -W/2  # starting at the top of the lip
z_snowboarder = a * y_snowboarder**2 + elevation_adjustment

v_y = 0  # Initial vertical velocity
v_x = 0  # Initial horizontal velocity

trajectory = [(x_snowboarder, y_snowboarder, z_snowboarder)]

while x_snowboarder < L:  # Until we reach the right end
    # Forces
    F_gravity_y = -2 * a * y_snowboarder * g  # gravitational force due to parabolic shape in Y direction
    F_slope_x = g_slope  # constant force due to slope in X direction
    
    # Net acceleration
    a_y = F_gravity_y
    a_x = F_slope_x
    
    # Update velocities
    v_y += a_y * dt
    v_x += a_x * dt
    
    # Update positions
    x_snowboarder += v_x * dt
    y_snowboarder += v_y * dt
    z_snowboarder = a * y_snowboarder**2 - x_snowboarder * np.tan(np.deg2rad(18)) + elevation_adjustment
    
    trajectory.append((x_snowboarder, y_snowboarder, z_snowboarder))

trajectory = np.array(trajectory)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot half-pipe
ax.plot_surface(X, Y, Z, color='b', alpha=0.5)

# Plot trajectory of the snowboarder
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 'r', linewidth=2)

# Plot projection on the ground
ax.plot(trajectory[:, 0], trajectory[:, 1], np.zeros_like(trajectory[:, 0]), 'b--', linewidth=2)

ax.set_xlabel('X axis (along the pipe)')
ax.set_ylabel('Y axis (width of pipe)')
ax.set_zlabel('Z axis (height)')
ax.set_box_aspect([np.ptp(trajectory[:, 0]), np.ptp(trajectory[:, 1]), np.ptp(Z)])  # Equal scaling for x, y, z

plt.title('Half-pipe, Trajectory of the Snowboarder, and its Projection')
plt.show()
