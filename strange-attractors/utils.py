from math import cos, sin, pi, floor, sqrt
from .glm.normalize import normalize

def __rotate__(point, vec_from, vec_to):
    """
    Rotates a point from 1 vector to another.
    """
    # Create rotation matrix
    # m = Mat4()
    # Multiply w/ point
    # return m.mul(point)
    return NotImplemented


def __gen_circle__(point=[0, 0, 0], resolution=4, radius=0.1, normal=[1, 0, 0]):
    """
    Generate a circle around a point acording to a given normal.

    """
    verts = []
    normals = []

    for i in range(0, resolution):

        # Generate point with circle normal on +x axis
        angle = i / resolution
        xx = cos(angle * 2 * pi)
        yy = sin(angle * 2 * pi)
        cur_vert = [xx * radius, yy * radius, 0]
        cur_norm = [xx, yy, 0]

        # Multiply by transform matrix based on normal
        cur_vert = __rotate__(cur_vert, [1, 0, 0], normal)
        cur_norm = __rotate__(cur_norm, [1, 0, 0], normal)

        # And add to VBO
        verts.extend(cur_vert)
        normals.extend(cur_norm)

    return (verts, normals)


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
    num_points = floor(len(points) / 3)
    for i in num_points:
        cur_point = [
            points[num_points * i],
            points[num_points * i + 1],
            points[num_points * i + 2]
        ]
        normal = []

        if (i < num_points - 1):
            normal = [
                cur_point[0] - points[num_points * (i + 1)],
                cur_point[1] - points[num_points * (i + 1) + 1],
                cur_point[2] - points[num_points * (i + 1) + 2]
            ]
        else:
            normal = [
                cur_point[0] - points[num_points * (i - 1)],
                cur_point[0] - points[num_points * (i - 1) + 1],
                cur_point[0] - points[num_points * (i - 1) + 2]
            ]

        # ➡️ normalize normal vector
        normal = normalize(normal)

        (circle_verts, circle_norms) = __gen_circle__(
            cur_point, resolution, radius, normal)

        vertices.extend(circle_verts)
        normals.extend(circle_norms)

        if (i > 1):
            for c in resolution:
                # Middle Rings
                prev_row = resolution * (i - 1)
                cur_row = resolution * i
                triangles.extend([
                    prev_row + c, prev_row + c + 1, cur_row + c,
                    cur_row + c, prev_row + c + 1, cur_row + c + 1
                ])

    return (vertices, triangles, normals)
