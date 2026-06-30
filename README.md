# AI Tools Learning

This repository contains my notes and hands-on implementations while learning **Built-in Tools** and **Custom Tools** using LangChain.

The goal is to understand how tools work, how they interact with LLMs, and how they are used to build AI applications.

## What I've Learned

* Built-in Tools
* Custom Tools
* Tool Metadata (`name`, `description`, `args`)
* Manual Tool Invocation
* Connecting a Custom Tool to a SQLite Database
* Using an LLM to process tool outputs

## Files

```text
built_in_tool.py      # Web search using Tavily
custom_tool.py        # Custom tool connected to SQLite
create_database.py    # Creates the SQLite database from CSV
test_database.py      # Tests database queries
players.csv           # Sample player dataset
players.db            # SQLite database (generated locally)
```

## Tech Stack

* Python
* LangChain
* Mistral AI
* Tavily Search
* SQLite
* Pandas

## Learning Flow

```text
Built-in Tool
      ↓
Custom Tool
      ↓
Database Integration
      ↓
Tool Binding
      ↓
Tool Calling
      ↓
LLM
      ↓
Final Response
```
More concepts and implementations will be added as I continue learning.

More concepts and implementations will be added as I continue learning.
