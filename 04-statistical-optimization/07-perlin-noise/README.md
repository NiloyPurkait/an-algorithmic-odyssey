# Perlin Noise

Ken Perlin developed gradient noise in the early 1980s for computer graphics, where purely random pixels looked harsh and artificial. Perlin noise creates randomness with continuity, so nearby coordinates have related values. Layered octaves turn that smooth noise into terrain, texture, and motion.

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
