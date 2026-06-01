# Voronoi Diagrams and Delaunay Triangulation

Voronoi diagrams partition the plane by nearest site. Delaunay triangulations connect sites that are natural neighbors under that partition. The lesson extends graph thinking into continuous space: proximity itself creates cells, adjacencies, and useful data structures.

## Open

- [voronoi-delaunay.ipynb](voronoi-delaunay.ipynb)

## What To Watch

- A Voronoi cell contains every point closer to one site than to any other.
- Delaunay edges correspond to shared Voronoi boundaries.
- Empty circumcircle tests identify valid Delaunay triangles.
- Duplicate points and co-circular points are common sources of numerical edge cases.

## Read Next

- [SciPy spatial algorithms documentation](https://docs.scipy.org/doc/scipy/reference/spatial.html) - Voronoi, Delaunay, convex hulls, and KD-trees.
- [Qhull project](http://www.qhull.org/) - geometry engine used by SciPy and other tools.
- [CGAL 2D Triangulations documentation](https://doc.cgal.org/latest/Triangulation_2/index.html) - robust computational-geometry reference.
