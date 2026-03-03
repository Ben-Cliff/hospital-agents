# Academic Research Sample Analysis

Based on the [ADK Academic Research Sample](https://github.com/google/adk-samples/tree/main/python/agents/academic-research), the system is built as a **Multi-Agent** ecosystem with the following characteristics:

### 1. Key Components
- **Orchestrator Agent:** Coordinates the research workflow.
- **WebSearch Sub-Agent:** Uses Google Search to find recent citations and academic publications.
- **NewResearch Sub-Agent:** Synthesizes original paper analysis with new findings to propose future research.

### 2. Implementation Workflow
1. **Analyze:** Extract core innovations and context from seminal papers (PDFs/URLs).
2. **Search:** Map influence by finding recent citations (e.g., papers citing "Attention Is All You Need").
3. **Propose:** Synthesize gaps and suggest novel research directions.

### 3. Core Tools
- **Google Search Retrieval:** For mapping contemporary influence.
- **PDF Analysis:** To ingest and parse internal/external documents.
- **Agent-as-a-Tool (A2A):** Connecting specialized sub-agents for search and synthesis.
