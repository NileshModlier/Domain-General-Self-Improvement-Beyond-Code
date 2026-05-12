Most self‑improving agent systems assume that skill at coding implies skill at self‑modification. This assumption holds for benchmarks like SWE‑bench, but fails to address non‑coding domains such as:

Review quality
Curriculum design
Explanation clarity
Policy reasoning

This project rigorously tests whether self‑improving agents can meaningfully evolve in domains where success is subjective, noisy, or preference‑based.

Motivation
If self‑improvement only works where:

Tasks are executable
Rewards are clean
Outputs are programmatically testable

Then claims of general agent self‑improvement are overstated.
This repository explores what breaks when those assumptions are removed.

Methodology
The project extends a DGM‑style agent by:

Replacing code execution metrics with pairwise preference evaluations
Using ensemble judges for noisy feedback
Measuring stagnation, regression, and instability

Domains tested include:

Paper reviewing
Curriculum generation
Structured reasoning tasks


Results
Key observations:

Agents often plateau rapidly without strong inductive bias
Preference‑based feedback dramatically increases variance
Some tasks show oscillation instead of monotonic improvement

This suggests that self‑improvement is domain‑dependent, not universally transferable.

Implications

Coding benchmarks alone are insufficient to assess general agent autonomy
Evaluation design is as important as agent architecture
Future systems require hybrid evaluation scaffolds
