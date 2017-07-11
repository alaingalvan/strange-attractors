def lorenz(num_points=15000, start=[0.10, 0.10, 0.10], scaling_factor=20, delta=0.008, a=0.1, b=4.0, c=14.0, d=0.08):
    """
    Generates Lorenz strange attractor.
    """
    verts = []
    x = start[0]
    y = start[1]
    z = start[2]

    for i in range(0, num_points):

        # calculate delta values
        dx = -a * x + (y * y) - (z * z) + a * c
        dy = x * (y - b * z) + d
        dz = z + x * (b * y + z)

        # calculate new coordinates
        x = x + delta * dx
        y = y + delta * dy
        z = z + delta * dz

        # scale and add them to the list
        verts.extend([
            x * scaling_factor, z * scaling_factor, y * scaling_factor
        ])

    return verts
