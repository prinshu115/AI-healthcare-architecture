## Data Flow

1. Data enters the system through approved sources only (EHR extracts, documents).
2. PHI is classified and redacted where required.
3. Text is chunked using clinically meaningful boundaries.
4. Embeddings are generated and stored in a vector database.
5. Retrieval is scoped and logged for audit.
6. LLM responses are validated before exposure.

Every step leaves an audit trail.