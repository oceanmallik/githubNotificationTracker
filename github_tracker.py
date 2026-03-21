import requests
import os

# 1. The Key (Authentication)
TOKEN = os.getenv("GITHUB_PAT")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def check_notifications():
    if not TOKEN:
        print("❌ Error: GITHUB_PAT environment variable is not set. See README.md file for more instruction. ")
        return

    # 2. The Request (Making the Call)
    url = "https://api.github.com/notifications"
    response = requests.get(url, headers=HEADERS)

    # 3. The Delivery (Checking if it worked and getting the JSON)
    if response.status_code == 200:
        notifications = response.json()
        
        # 4. The Translation (Parsing the Data)
        if not notifications:
            print("🎉 You have no unread notifications!")
        else:
            print(f"📫 You have {len(notifications)} unread notifications:\n")
            for item in notifications:
                repo_name = item['repository']['full_name']
                issue_title = item['subject']['title']
                print(f"- [{repo_name}] {issue_title}")
    else:
        print(f"❌ Failed to connect. GitHub said: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    check_notifications()
