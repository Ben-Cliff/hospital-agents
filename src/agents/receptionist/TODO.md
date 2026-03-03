# Receptionist Agent TODOs

### `agent.py`
- [ ] **Update System Prompt**: Modify the prompt to instruct the receptionist to handle researching existing schedules and medication collection status.
- [ ] **Register Tools**: Add the new tools (once created) to the `tools` list in the `Agent` initialization.

### `tools.py`
- [ ] **Add Tool - Check Existing Appointments**: Create a tool to check existing appointments for a patient. 
  - *Hint*: Maintain an in-memory "database" (dictionary) mapping patient names to their upcoming appointments and query it.
- [ ] **Add Tool - Check Medication Collection Status**: Create a tool to check the status of medication collection for a patient. 
  - *Hint*: Maintain an in-memory "database" (dictionary) mapping patient names to their medication collection status (e.g., "collected", "pending", "not collected") and query it.
