import math
# 1 Physical constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho = 1.225  # Density of air at sea level (kg/m^3)

# 2 Projectile Inputs 
mass = 10.0  # vehicle mass (kg)
area = 0.05  # cross-sectional area (m^2)
cd = 0.47 # Drag coefficient (dimensionless)

# 3 Initial launch conditions
v0 = 100 #launch speed (m/s)
angle_deg = 45.0 # launch angle (degrees)

# Convert launch angle to radians for math functions
angle_rad = math.radians(angle_deg)

# Calculate horizontal and vertical components of the initial velocity
v0x = v0 * math.cos(angle_rad)  # Horizontal component of initialvelocity (m/s)
v0y = v0 * math.sin(angle_rad) # Vertical component of initial velocity (m/s)

# Output summary 
print("--- Trajectory Simulation Summary ---")
print(f"Initial Velocity: {v0:.2f} m/s at {angle_deg} degrees")
print(f"Horizontal Velocity (v0x): {v0x:.2f} m/s")
print(f"Vertical Velocity: {v0y:.2f} m/s")

