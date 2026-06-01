# Perlin Noise

Perlin noise produces coherent randomness: nearby coordinates tend to have related values. Read as a signal, it is frequency synthesis: stacking octaves layers low- and high-frequency detail, making Perlin the constructive counterpart to the Fourier transform's analysis. Here, probabilistic structure becomes a material students can draw with: terrain, texture, and motion.

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
