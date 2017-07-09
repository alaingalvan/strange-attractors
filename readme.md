![Strange Attractor Cover](https://alain.xyz/libraries/coronal/assets/cover.jpg)

# Strange Attractors

[![Download][download-img]][download-url]
[![License][license-img]][license-url]

Algorithms to generate strange attractors. Use these algorithms to create **Vertex Buffer Objects** and **Index Buffer Objects** for your graphics API of choice.

## Usage

Each attractor function returns an array of vertex points in the format `[x1, y1, z1, x2, y2, z2, ...]`, from there you can use the included `spline_mesh` function to convert that data to a Vertex Buffer and Index Buffer:

```py
from strange_attractors import burgers, spline_mesh

(triangles, vertices, normals) = spline_mesh(burgers(), 4, 0.05)
  ```

## API

### Attractors

#### Burgers

`burgers(num_points=10000, start=[0.5, 0.5, 0.5], factor=250, radius=0.1, a=0.7, b=0.78)`

| Arguments | Type | Description |
|-----------|------|-------------|
| `num_points`| `long` | Number of points |
| `start`| `float[3]` | Starting vector |
| `factor`| `long` | Rotation factor |
| `radius`| `float` | Radius of burger |
| `a`| `float` | Alpha constant |
| `b`| `float` | Beta constant |

**Returns:** `float[3*num_points]`

A round loopy shape, which looks a lot like a burger (hence the name).

```py
def burgers(num_points=10000, start=[0.5, 0.5, 0.5], factor=250, radius=0.1, a=0.7, b=0.78):
```

### Utilities

#### Spline Mesh

`spline_mesh(points=[], resolution=4, radius=0.1)`

| Arguments | Type | Description |
|-----------|------|-------------|
| `points`| `float[3*N]` | Input points |
| `resolution`| `unsigned long` | Resolution of spline rings |
| `radius`| `float` | Radius of spline |

**Returns:** `(long[3*N], float[3*N], float[3*N])`

 Generates a VBO/IBO for a given spline.

[license-img]: http://img.shields.io/:license-unlicense-blue.svg?style=flat-square
[license-url]: http://unlicense.org/
[download-img]: http://img.shields.io/:download-🡣-gray.svg?style=flat-square
[download-url]: https://github.com/alaingalvan/strange-attractors/archive/master.zip