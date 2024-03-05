import cmath

# Create a complex number
z = complex(3, 4)  # 3 + 4j

# Access real and imaginary parts
real_part = z.real  # 3.0
imaginary_part = z.imag  # 4.0

# Perform operations with complex numbers
w = complex(1, -2)
result = z + w  # (3 + 4j) + (1 - 2j) = 4 + 2j

# Other operations, such as multiplication, division, etc., can also be performed.

# Calculate the magnitude (absolute value) of a complex number
magnitude = abs(z)  # sqrt(3^2 + 4^2) = 5.0

# Calculate the phase angle of a complex number in radians
phase_angle = cmath.phase(z)  # atan2(4, 3) = 0.93 radians

# Convert polar coordinates to a complex number
r = 5
theta = 0.93
polar_complex = cmath.rect(r, theta)  # 3 + 4j

# Conjugate of a complex number
conjugate_z = cmath.conj(z)  # 3 - 4j
