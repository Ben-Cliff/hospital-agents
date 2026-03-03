# Project Migration Challenge: Building a Multi-Agent Hospital System

Welcome to the migration challenge. This guide outlines the transformation of our single-agent RAG prototype into a sophisticated, modular multi-agent ecosystem. Your mission is to re-engineer the system into a coordinated team of specialized agents.

**The Goal:** Create a scalable hospital assistant with a **Medical Expert**, an **Administrative Receptionist**, and a **Deep Researcher**, all managed by a **Master Orchestrator**.

---

## Challenge 1: Codebase Sanitization (A Clean Slate)

First, let's clear out the old scaffolding to make way for the new architecture.

*   **Task:** Scan all files in the `src/` directory and remove every comment and code block tagged with `# TODO: HACKATHON CHALLENGE`.
*   **Task:** Once sanitized, this `CHALLENGE.md` file will be deleted, as its purpose will be fulfilled.

---

## Challenge 2: Architecting the Agent Squad (Directory Restructure)

To ensure each agent can be developed in isolation, we need to restructure the `src/agents/` directory.

**Your Goal:**
Create a modular directory structure that houses each agent's unique persona and toolset.

**Where to Hack:**
*   Create the following subdirectories inside `src/agents/`:
    ```text
    src/agents/
    ├── doctor/
    ├── receptionist/
    ├── researcher/
    └── master/
    ```

---

## Challenge 3: Building the Specialists (Agent Development)

Now it's time to build the core of our new system: the specialized agents.

### Part A: The Doctor Agent (The RAG Specialist)

Transform the existing agent into a medical reasoning expert.

*   **Location:** `src/agents/doctor/`
*   **Task 1 (Tool Migration):** Move the existing `search_knowledge_base` tool logic into a new `src/agents/doctor/tools.py`.
*   **Task 2 (Persona Upgrade):** Create an `agent.py` in the directory and give it a high-fidelity "Clinical Resident" persona. The new instructions must prioritize grounding—strictly citing sources from the RAG tool and explicitly stating when information is missing.

### Part B: The Receptionist Agent (The Action Taker)

Enable the system to interact with external administrative systems.

*   **Location:** `src/agents/receptionist/`
*   **Task 1 (MCP Implementation):** Implement a new tool in `src/agents/receptionist/tools.py` for appointment scheduling. You'll need to use the **Model Context Protocol (MCP)** libraries already in the environment.
*   **Task 2 (Persona Focus):** Define a "Hospital Receptionist" persona in `agent.py` focused on gathering missing information (e.g., `patient_name`, `appointment_time`) from the user before executing a tool call.

### Part C: The Researcher Agent (The Academic Explorer)

Bridge the gap between the hospital’s private data and global clinical knowledge.

*   **Location:** `src/agents/researcher/`
*   **Task 1 (External Tooling):** Implement a tool in `src/agents/researcher/tools.py` that interfaces with Google Search (via Vertex AI Search or a public search API).
*   **Task 2 (Persona Focus):** Create a "Medical Researcher" persona in `agent.py` that can synthesize internal data with external search results to answer technical queries.

---

## Challenge 4: Assembling the Team (The Master Orchestrator)

With the specialists built, it's time to create the "Final Boss"—the primary interface that manages task delegation.

**Your Goal:**
Build a master agent that uses the other agents as tools, intelligently routing user requests to the correct specialist.

**Where to Hack:**
*   **`src/agents/master/agent.py`**:
    *   **Task 1 (A2A Integration):** Create the master agent configuration. Use the ADK's **Agent-as-a-Tool** feature to pass the Doctor, Receptionist, and Researcher agents into its `tools` parameter.
    *   **Task 2 (Triage Logic):** Define instructions for the Master Agent to act as a **Triage Specialist**. It must determine user intent and delegate the query to the correct sub-agent.

---

## Challenge 5: Polishing the System (Docs & Finalization)

The final step is to update all documentation and configuration to reflect the new multi-agent architecture.

**Tasks:**

1.  **Documentation Overhaul:**
    *   **`README.md`:** Rewrite the "How It Works" section to explain the new Orchestrator/sub-agent interaction.
    *   **`AGENT_ARCHITECTURE.md`:** Create this new file to detail the Agent-to-Agent (A2A) flow and how the Master Agent uses sub-agents as tools.

2.  **Infrastructure & Setup:**
    *   **`INFRASTRUCTURE_SETUP.md`:** Revise the guide to include any new environment variables required for the Receptionist's MCP tools or the Researcher's search tools.
    *   **`.env.example`:** Update the template to include placeholders for `ENGINE_ID` and any new API keys, ensuring they are marked as required.

3.  **Finalizing the Entrypoint:**
    *   **`main.py`:** Update the application's entrypoint to import and run the `master_agent` from `src.agents.master.agent`.
    *   **Verification:** Ensure the `InMemoryRunner` initializes the multi-agent loop correctly, allowing the Master Agent to call sub-agents without crashing.