# Voronoi Diagrams and Delaunay Triangulation

Voronoi diagrams are named for Georgy Voronoi's early twentieth-century work, with older roots in Dirichlet's geometric partitions. The question is simple and useful. Which site is closest to each point in space? The paired Delaunay triangulation turns those regions into neighbor relationships for interpolation, meshes, maps, and spatial queries.

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
