# Grover's Algorithm

Grover's algorithm gives the simplest visual entry into quantum speedup. An oracle marks one answer, diffusion reflects amplitudes about their mean, and repeated rotations concentrate probability on the target. The square-root query advantage appears alongside the over-rotation failure mode.

## Open

- [grovers-algorithm.ipynb](grovers-algorithm.ipynb)

## What To Watch

- One Grover iteration is two reflections: the oracle flips the sign of the marked state, and the diffusion step inverts every amplitude about the mean.
- On 8 states the target probability climbs `0.125 -> 0.781 -> 0.945` over the first two iterations.
- The state lives in a 2D plane and rotates by `2*theta` toward the answer each step, which is why about `(pi/4) * sqrt(N)` iterations suffice - the square-root speedup.
- Over-rotation is the failure mode: too many iterations swing past the target and the success probability falls, so the algorithm must stop at the first peak.

## Read Next

- [Grover, A Fast Quantum Mechanical Algorithm for Database Search](https://doi.org/10.1145/237814.237866) - the original algorithm.
- [Nielsen and Chuang, Quantum Computation and Quantum Information](https://doi.org/10.1017/CBO9780511976667) - quantum search and amplitude amplification (chapter 6).
- [Brassard, Hoyer, Mosca, and Tapp, Quantum Amplitude Amplification and Estimation](https://doi.org/10.1090/conm/305/05215) - the general framework behind Grover.
