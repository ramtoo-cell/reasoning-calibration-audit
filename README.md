# Calibration and Abstention Audit

When should a reasoning system abstain instead of answering confidently?

**Status: v0.1 research prototype.** Standard-library Python 3.9+; no API keys, paid calls, or network access needed. The included data is synthetic and demonstrates behavior, not measured model capability.

## Run in 30 seconds

```sh
python3 cli.py example.json
python3 -m unittest -v
```

Run from the repository directory. Replace `example.json` with your own file using the same fields. The CLI writes JSON to stdout; invalid input exits with status 2. See `example-output.json` for the checked demonstration output.

## What it does

Compute binary correctness Brier score, equal-width expected calibration error, and tie-aware risk/coverage points. Confidence is the estimated probability that the chosen answer is correct.

## Input contract

`example.json` is a complete minimal input. `engine.analyze(data)` exposes the same functionality as a Python API. Additional optional parameters and validation are visible in `engine.py`. Numerical rates are fractions, not percentages. Missing required fields are rejected by the CLI.

## Interpretation and limits

Self-reported confidence may not be meaningful. Thresholds selected on evaluation data are exploratory; validate on a held-out set before deployment. ECE depends on binning.

## Research workflow

1. Define a domain-specific question and success criteria before collecting outputs.
2. Separate development examples from the held-out evaluation set.
3. Record the exact model version, prompts, decoding settings, tools, dates, and dataset provenance.
4. Run this analyzer on independently checked outcomes. Preserve disagreements and negative results.
5. Report denominators, uncertainty where applicable, and the scope in which conclusions hold.

## Reproducibility

`test_engine.py` covers known-answer cases and failure conditions. `example-output.json` was generated from the included synthetic input. `METHODS.md` records assumptions and an experiment proposal. `DATA_CARD.md` describes provenance. `PROVENANCE.md` discloses AI assistance.

This project is independent and is not affiliated with or endorsed by Anthropic or OpenAI. It does not claim published research, production readiness, or results on either company's models.
