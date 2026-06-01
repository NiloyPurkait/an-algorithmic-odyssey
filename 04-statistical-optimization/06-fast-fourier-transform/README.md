# Fast Fourier Transform

Fourier analysis turns signals into frequency components, a language used across physics, audio, imaging, and numerical computation. Cooley and Tukey's 1965 FFT paper made a fast divide-and-conquer transform central to digital computing, though related ideas are older. Symmetry in roots of unity reduces repeated work.

## Open

- [fft.ipynb](fft.ipynb)

## What To Watch

- The DFT compares a signal against complex sinusoids.
- Cooley-Tukey splits the problem into even and odd indices.
- Reused twiddle factors are where the speedup comes from.
- The runtime drops from `O(n^2)` for direct DFT computation to `O(n log n)` for common FFT sizes.

## Read Next

- [Cooley and Tukey, An Algorithm for the Machine Calculation of Complex Fourier Series](https://doi.org/10.1090/S0025-5718-1965-0178586-1) - landmark FFT paper.
- [FFTW documentation](https://www.fftw.org/) - high-performance FFT library.
- [BetterExplained: An Interactive Guide to the Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/) - intuition for frequency-domain thinking.
