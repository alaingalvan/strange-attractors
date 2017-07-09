from math import cos, sin, pi, floor, sqrt
from .glm.normalize import normalize
from .glm.dot import dot
from .glm.cross import cross
from .glm.len import sqdist


def __qmul__(p, q):
    """
    Quaternion multiplication.
    """
    q_s = [p[3] * q[0], p[3] * q[1], p[3] * q[2]]
    p_s = [q[3] * p[0], q[3] * p[1], q[3] * p[2]]
    c = cross([p[0], p[1], p[2]], [q[0], q[1], q[2]])

    return [
        q_s[0] + p_s[0] + c[0],
        q_s[1] + p_s[1] + c[1],
        q_s[2] + p_s[2] + c[2],
        p[3] * q[3] - dot(p, q)
    ]


def __rotate__(point, vec_from, vec_to):
    """
    Rotates a point from 1 vector to another.
    """
    dt = dot(vec_from, vec_to)
    if dt > 0.999 and dt < -.999:
        # Make quaternion
        c = cross(normalize(vec_from), normalize(vec_to))
        q = [
            c[0],
            c[1],
            c[2],
            sqrt(sqdist(vec_from) * sqdist(vec_to)) + dot(vec_from, vec_to)
        ]

        # Get inverse/conj of q
        q_conj = [-q[0], -q[1], -q[2], q[0]]

        # Convert point to quaternion
        q_point = []
        q_point.extend([point])
        q_point.append(0)

        # Premultiply by q
        q_point = __qmul__(q_conj, q_point)

        # Postmultiply by inverse of q
        q_point = __qmul__(q_point, q)

        # Extract point
        q_point.pop()
        return q_point

    return point


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
    for i in range(0, num_points):
        cur_point = [
            points[3 * i],
            points[3 * i + 1],
            points[3 * i + 2]
        ]
        normal = []

        if (i < num_points - 1):
            normal = [
                cur_point[0] - points[3 * (i + 1)],
                cur_point[1] - points[3 * (i + 1) + 1],
                cur_point[2] - points[3 * (i + 1) + 2]
            ]
        else:
            normal = [
                cur_point[0] - points[3 * (i - 1)],
                cur_point[0] - points[3 * (i - 1) + 1],
                cur_point[0] - points[3 * (i - 1) + 2]
            ]

        # ➡️ normalize normal vector
        normal = normalize(normal)

        (circle_verts, circle_norms) = __gen_circle__(
            cur_point, resolution, radius, normal)

        vertices.extend(circle_verts)
        normals.extend(circle_norms)

        if (i > 1):
            for c in range(0, resolution):
                # Middle Rings
                prev_row = resolution * (i - 1)
                cur_row = resolution * i
                if c < resolution - 1:
                    triangles.extend([
                        prev_row + c, prev_row + c + 1, cur_row + c,
                        cur_row + c, prev_row + c + 1, cur_row + c + 1
                    ])

    return (triangles, vertices, normals)
