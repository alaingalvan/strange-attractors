# Strange Attractors

[![Download][download-img]][download-url]
[![License][license-img]][license-url]

Algorithms to generate strange attractors. Use these algorithms to create Vertex Buffer Objects for your graphics API of choice.

## Usage

Each attractor function returns an array of vertex points in the format `[x1, y1, z1, x2, y2, z2, ...]`, from there you can use the included `spline_mesh` function to convert that data to a Vertex Buffer and Index Buffer:

```py
import lorenz, spline_mesh from strange_attractors

(vertices, triangles, normals) = spline_mesh(lorenz(), 4, 0.1)
  ```

[license-img]: http://img.shields.io/:license-unlicense-blue.svg?style=flat-square
[license-url]: http://unlicense.org/
[download-img]: http://img.shields.io/:download-🡣-gray.svg?style=flat-square
[download-url]: https://github.com/alaingalvan/strange-attractors/archive/master.zip