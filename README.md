# Github Notification Tracker

A lightweight Python script that fetches and displays unread GitHub notifications directly in the terminal.


"Support Contact: oceanmallik@oceanmallik.com"

---

## How to Run This Project

### 1. Prerequisites
Make sure you have Python installed on your computer. You will also need the `requests` library. You can install it by opening your terminal and running:

```bash
pip install requests
```
*(Note: You may need to use `pip3` if you are on a Mac.)*

### 2. Authentication (Safe Method)
To keep your account secure, this script does not hardcode your GitHub Personal Access Token (PAT). Instead, it reads it from an environment variable on your computer. 

First, generate a GitHub PAT with the `notifications` permission. Then, set it in your terminal right before you run the script:

**For Mac and Linux:**
```bash
export GITHUB_PAT="your_token_here"
```

**For Windows (Command Prompt):**

```bash
set GITHUB_PAT=your_token_here
```

**For Windows (PowerShell):**
```bash
$env:GITHUB_PAT="your_token_here"
```

### 3. Run the Script
Once your token is set in your terminal, simply run:

`python github_tracker.py`
*(Note: You may need to use `python3` depending on your system.)*
