# Github Notification Tracker

A lightweight Python script that fetches and displays unread GitHub notifications directly in the terminal.


"Support Contact: oceanmallik@oceanmallik.com"

---

## How to Get Your Personal Access Token (PAT)
Before you can run this script, you need a secure token so it can read your notifications. 

1. Log in to GitHub and click your profile picture in the top right corner.
2. Select **Settings** from the dropdown menu.
3. Scroll to the very bottom of the left sidebar and click **Developer settings**.
4. Click **Personal access tokens** on the left menu, then select **Tokens (classic)**.
5. Click the **Generate new token** button and choose **Generate new token (classic)**.
6. Type a note like "Notification Tracker" so you remember what it is for.
7. Scroll down the list of permissions and check the box next to **notifications**.
8. Scroll to the bottom and click **Generate token**.
9. **Copy the token immediately!** GitHub will never show it to you again.

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

```bash
python github_tracker.py
```
*(Note: You may need to use `python3` depending on your system.)*
