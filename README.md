# Git2Azure-Bonus-task

## Problem Statement & Use Case

### **Problem Statement**
This project introduces **ASI1mini Agent**, a local AI agent capable of receiving user queries, processing them, and responding appropriately.

### **Use Case Description**
The ASI1mini Agent acts as a query-processing assistant that:
1. Accepts user input (queries) via the console.
2. Sends the query as a message to itself for processing.
3. Logs and responds to the query asynchronously.
4. Implements startup and shutdown behaviors, ensuring smooth agent lifecycle management.

This architecture is useful for:
- AI-powered chatbots.
- Automated information retrieval systems.
- Decentralized agent-based networks.

---

## System Architecture

Below is a high-level system architecture diagram for ASI1mini Agent:

```
+------------------+
|  User Input     |
|  (Console)      |
+------------------+
        |
        v
+------------------+
|  ASI1mini Agent |
|  (Local Agent)  |
+------------------+
        |
        v
+------------------+
|  Message Handler|
|  (Processes &   |
|  Responds to    |
|  Queries)       |
+------------------+
```

---

## List of Agents

### **Local Agents:**
- **ASI1mini Agent (Agent 2009)**
  - Name: `Agent 2009`
  - Port: `2009`
  - Role: Handles user queries and logs responses
  - Communication: Local

### **AgentVerse Agents:**
- *None at the moment, but future iterations may include external agents for query processing or knowledge retrieval.*

---

## Usage Examples

### **Setup & Running the Agent**
Ensure you have Python and `uagents` installed:
```bash
pip install uagents
```

Run the agent:
```bash
python agent_2009.py
```

### **Agent Interaction**
1. The agent will start and prompt the user for a query.
2. Enter a query, e.g.:
   ```
   Enter Your Query...= What is the meaning of life?
   ```
3. The agent will send and log the response:
   ```
   INFO: Hello Boss!, I am Agent 2009
   INFO: Hello, My Address is agent1xyz...
   INFO: What is the meaning of life?
   ```

### **Shutting Down**
When the agent is stopped, it prints an ASCII-style "BYE" message:
```
  ______                  ________
||      \    \\    //   ||
||      /     \\  //    ||
||======       \\//     ||_____
||      \       ||      ||
||       |      ||      ||
||______/       ||      ||________
```

---

## Future Enhancements
- **Multi-agent communication**: Extend the agent to interact with external AgentVerse agents.
- **Persistent Query Storage**: Store queries and responses for future reference.
- **Web Interface**: Replace console input with a web UI.

This agent serves as a foundational building block for AI-powered decentralized systems. 🚀

