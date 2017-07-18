def burgers(num_points=2000, start=[0.5, 0.5, 0.5], factor=250, delta=0.1, a=0.7, b=0.78):
    """
    Generates Burger strange attractor.
    """

    verts = []
    zp = 0
    zq = 0
    xa = start[0]
    y = start[1]
    for i in range(0, num_points):
        x = (1.0 - a) * xa - y * y
        y = (1.0 + b) * y + xa * y
        verts.extend([
            x * factor - radius, y * factor - radius, 0,
            x * factor - radius, y * factor + radius, 0,
            x * factor + radius, y * factor + radius, 0,
            x * factor + radius, y * factor - radius, 0
        ])
        xa = x
    return verts
