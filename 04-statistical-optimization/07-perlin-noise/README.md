# Perlin Noise

Perlin noise creates randomness with continuity, which is why it works for terrain, texture, and motion. Gradients on a lattice are interpolated smoothly, then layered across octaves for detail at multiple scales. Procedural noise becomes constructive signal synthesis.

## Open

- [perlin-noise.ipynb](perlin-noise.ipynb)

## What To Watch

- Gradient vectors are assigned to lattice points.
- Interpolation smooths values between lattice points.
- Octaves combine multiple frequencies into layered detail.
- A seed makes the generated result repeatable.

## Read Next

- [Perlin, An Image Synthesizer](https://dl.acm.org/doi/10.1145/325165.325247) - original SIGGRAPH paper.
- [Perlin, Improving Noise](https://dl.acm.org/doi/10.1145/566570.566636) - later refinement.
- [Scratchapixel: Perlin Noise](https://www.scratchapixel.com/lessons/procedural-generation-virtual-worlds/perlin-noise-part-2/perlin-noise.html) - implementation walkthrough.
