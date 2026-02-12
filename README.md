# 🚀 Code Refactor Assistant

A lightweight static code analysis tool built using Python and AST (Abstract Syntax Tree) to detect structural code issues and suggest refactoring improvements.
---
## 🔍 Features

- Detects long functions
- Identifies nested loops (O(n²) risk)
- Flags too many function parameters
- Detects unclear variable names
- Provides refactoring suggestions
- Clean Streamlit UI
---
## 🛠 Tech Stack
- Python
- AST (Abstract Syntax Tree)
- Streamlit
---
## ⚙️ How It Works
1. User pastes Python code.
2. Code is parsed using Python’s `ast` module.
3. The AST tree is traversed to detect structural issues.
4. Issues and improvement suggestions are displayed.
---
## ▶️ How To Run Locally
```bash
git clone <your-repo-link>
cd code-refactor-assistant
pip install -r requirements.txt
streamlit run app.py
