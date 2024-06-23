import requests

url = "https://chat-api.you.com/research"

payload = {
    "query": "Where is the restraut located in UCB for lunch with google map link?",
    "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
}
headers = {
    "X-API-Key": "92751b4d-8cfb-4cd4-a708-8a2689dcce3b<__>1PTsFeETU8N2v5f4qmtDZVGS",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)