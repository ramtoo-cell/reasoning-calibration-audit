# Method and experiment protocol

## Research question
When should a reasoning system abstain instead of answering confidently?

## Implemented method
Compute binary correctness Brier score, equal-width expected calibration error, and tie-aware risk/coverage points. Confidence is the estimated probability that the chosen answer is correct.

## Assumptions and failure modes
Self-reported confidence may not be meaningful. Thresholds selected on evaluation data are exploratory; validate on a held-out set before deployment. ECE depends on binning.

## Proposed next experiment — not yet performed
Collect a held-out set of expert-reviewed audit or policy reasoning tasks. Use stable task IDs, preregister the comparison, and record model and prompt versions. Double-review a subset, adjudicate disagreements, and publish anonymized artifacts only when permitted. Separate exploratory analysis from confirmatory results. The fixture is insufficient to estimate real-world performance.

## Scope
The implementation is deliberately inspectable. Validation checks common malformed inputs; it is not a hardened service for adversarial payloads. Apply external input-size limits for large files. No model API is called by this repository.
