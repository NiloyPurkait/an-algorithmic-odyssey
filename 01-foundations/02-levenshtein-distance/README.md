# Levenshtein Distance

Vladimir Levenshtein's mid-1960s work on error-correcting codes gave a precise way to reason about strings under editing errors. That language later became central to spell-checking, DNA sequence comparison, search, and record linkage. The version used here prices insertions, deletions, and substitutions, then fills a dynamic-programming table over prefixes so approximate matching becomes a traceable optimization problem.

## Open

- [levenshtein-distance.ipynb](levenshtein-distance.ipynb)

## What To Watch

- Each table cell describes two prefixes, not the whole strings.
- The recurrence compares the three possible last edits.
- Backtracking turns the final distance into an edit script.
- The basic dynamic program costs `O(mn)` time for strings of lengths `m` and `n`.

## Read Next

- [Wagner and Fischer, The String-to-String Correction Problem](https://doi.org/10.1145/321796.321811) - classic edit-distance dynamic program.
- [Jurafsky and Martin, Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) - NLP context for spelling, alignment, and distance.
- [MIT OCW 6.006 lecture notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) - dynamic programming in an algorithms course.
