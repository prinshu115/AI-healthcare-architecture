## RAG vs Fine-Tuning

This decision comes up early in every healthcare AI discussion.

Fine-tuning can look attractive but creates long-term risk:
- Knowledge becomes stale
- PHI exposure is harder to control
- Retraining cycles are expensive

RAG was chosen as the default approach because it keeps knowledge external,
traceable, and easier to update.

Fine-tuning is reserved for narrow, non-sensitive tasks.