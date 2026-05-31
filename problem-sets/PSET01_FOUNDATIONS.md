# Problem Set 1: Foundations

## Goals

By the end, students should be able to trace deterministic state, reason about growth, use a dynamic-programming table, explain a greedy choice, and connect computation to formal machines.

## Problems

### 1. Growth by Measurement and Model

Run two sorting methods on at least five input sizes. For each, collect operation counts or timings.

Deliverables:

- a plot of size versus cost
- one paragraph explaining the expected asymptotic shape
- one paragraph explaining where measurement noise appears

### 2. Sorting Trace

Use `courseware.bubble_sort_trace` or build your own trace for insertion sort, selection sort, or merge sort.

Deliverables:

- an interactive or frame-by-frame visual trace
- a count of comparisons and data moves
- one invariant that is visible in the animation

### 3. Antikythera Gear Ratios

Use the Antikythera notebook to study the ratio `64/38 * 48/24 * 127/32`.

Deliverables:

- exact fraction calculation
- explanation of why `254/19 - 1 = 235/19`
- visual crank output for 1 year, 19 years, and 1 Saros cycle
- one changed tooth count and the accumulated phase error after 19 years

### 4. Edit Distance as a Table Proof

Compute Levenshtein distance for three candidate corrections of the same misspelled word.

Deliverables:

- the filled matrix for each candidate
- the best correction under edit distance
- one case where edit distance alone might choose the wrong semantic correction

### 5. Huffman Exchange Argument

Compress two text samples: one skewed and one close to uniform.

Deliverables:

- the frequency table
- the resulting code lengths
- a proof sketch for why merging the two least frequent symbols is safe

### 6. Turing Machine Micro-Lab

Design a tiny Turing machine with at most four states.

Deliverables:

- transition table
- trace for at least 12 steps or until halting
- a short answer: what configuration fully describes the machine at any moment?

## Reflection

Choose one idea from this module and explain where it appears again in graph algorithms, optimization, or cryptography.
