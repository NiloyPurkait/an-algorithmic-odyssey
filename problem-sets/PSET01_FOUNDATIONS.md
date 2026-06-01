# Problem Set 1: Foundations

## Goals

Practice tracing deterministic state, reasoning about growth, using a dynamic-programming table, explaining a greedy choice, and connecting computation to formal machines.

## Problems

### 1. Growth by Measurement and Model

Run two sorting methods on at least five input sizes. For each method, collect operation counts or timings under the same hardware and input-generation procedure.

Deliverables:

- a plot of size versus cost
- one paragraph explaining the expected asymptotic shape
- one paragraph explaining where timing noise or input-order effects appear

### 2. Sorting Trace

Use `courseware.bubble_sort_trace` or build your own trace for insertion sort, selection sort, or merge sort.

Deliverables:

- an interactive or frame-by-frame visual trace
- a count of comparisons and data moves
- one invariant that is visible in the animation

### 3. Antikythera Gear Ratios

Use the Antikythera notebook to study the lunar gearing ratio `64/38 * 48/24 * 127/32`.

Deliverables:

- exact fraction calculation
- explanation of why `254/19 - 1 = 235/19`
- visual crank output for 1 year, 19 years, and 223 lunar months
- one changed tooth count and the accumulated phase error after 19 years

### 4. Edit Distance as a Table Proof

Compute Levenshtein distance for three candidate corrections of the same misspelled word.

Deliverables:

- the filled matrix for each candidate
- the best correction under edit distance
- one case where edit distance alone might choose the wrong correction because meaning or word frequency is missing

### 5. Huffman Exchange Argument

Compress two text samples with the same alphabet size: one skewed and one close to uniform.

Deliverables:

- the frequency table
- the resulting code lengths
- a proof sketch for why merging the two least frequent symbols is safe

### 6. Turing Machine Micro-Lab

Design a tiny Turing machine with at most four non-halting states.

Deliverables:

- transition table
- trace for at least 12 steps or until halting
- a short answer: what configuration fully describes the machine at any moment?

### 7. Recursive Substitution and Self-Similarity

Run Penrose tiling for at least three deflation depths.

Deliverables:

- tile count by depth and the growth ratio between successive depths
- visual comparison across depths
- one sentence on how a local substitution rule produces global non-periodic order

## Reflection

Choose one idea from this module and explain where it appears again in graph algorithms, optimization, or cryptography.
