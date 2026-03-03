# Orchestrator Agent Challenge: The Creative Orchestrator

The Orchestrator Agent is the front door to our hospital system. It doesn't perform medical diagnosis or schedule appointments itself. Instead, it acts as an **Orchestrator**, listening to the user and seamlessly delegating tasks to the specialized sub-agents.

This challenge focuses on the magic of **Agent-as-a-Tool (A2A)** and creative prompt engineering.

## Tasks

- [ ] **Define the Persona:**
    - Open `agent.py` and rewrite the `system_prompt`. Give the Orchestrator Agent a unique, highly memorable personality. Are they a friendly holographic greeter? A no-nonsense head triage nurse? Let your creativity run wild.

- [ ] **Connect the Sub-Agents:**
    - The `agent.py` skeleton currently has the sub-agents commented out. 
    - Import the `root_agent` from both `src/agents/doctor/agent.py` and `src/agents/receptionist/agent.py`.
    - Uncomment them in the `tools` list of the `orchestrator_agent`. This simple step enables the Orchestrator to treat other fully-featured agents as tools it can call upon!

- [ ] **Test the Multi-Agent Handoff:**
    - Once connected, test the orchestration with complex prompts.
    - Example: *"My head is pounding and I feel dizzy. Can you tell me what's wrong and book me the next available slot?"*
    - The goal is for the Orchestrator Agent to autonomously consult the Doctor for the medical advice, consult the Receptionist for the schedule, and weave their answers into a single, cohesive, in-character response.
