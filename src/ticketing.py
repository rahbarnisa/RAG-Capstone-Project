import requests

GITHUB_TOKEN = "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"
REPO = "rahbarnisa/RAG-Capstone-Project"

def create_github_issue(title, description):
    url = f"https://api.github.com/repos/{REPO}/issues"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "title": title,
        "body": description
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        return response.json()["html_url"]
    else:
        return f"Error: {response.text}"