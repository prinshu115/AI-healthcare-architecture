## System Overview

A healthcare AI system is never just an LLM.

At a minimum, the system consists of:
- Secure data ingestion
- Controlled retrieval
- LLM orchestration
- Evaluation and guardrails
- Human validation

The architecture is intentionally layered so that each concern can evolve
independently without breaking compliance or safety.

Key principle:
> Models are replaceable. Architecture mistakes are expensive.