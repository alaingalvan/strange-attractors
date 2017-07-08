from math import cos, sin, pi

def __gen_circle__(point=[0, 0, 0], resolution=4, radius=0.1, normal=[1, 0, 0]):
    """
    Generate a circle around a point acording to a given normal.
    """
    verts = []

    for i in range(0, resolution):
        angle = i / resolution
        xx = cos(angle * 2 * pi)
        yy = sin(angle * 2 * pi)
        cur_vert = [xx * radius, yy * radius, 0]
        verts.extend([xx * radius, yy * radius, 0])

    return verts


def spline_mesh(points=[], resolution=4, radius=0.1):
    """
    Generates a VBO/IBO for a given spline.

    Parameters
    ----------
    points : list of long
    A list of triples, [x1, y1, z1, x2, y2, z2, ...`]

    resolution: unsigned long
    The resolution of the spline circle (4 means square)

    radius: float
    The radius of the spline circle
    """
    vertices = []
    triangles = []
    normals = []

    for i in len(points):
        normal = []
        if (i < len(points)):
            normal = points[i] - points[i + 1]
        else:
            normal = points[i - 1] - points[i]

        circle = __gen_circle__(points[i], resolution, radius, normal)

        vertices.extend(circle)
        # Figure out triangles
        # Figure out normals

    return (vertices, triangles, normals)
