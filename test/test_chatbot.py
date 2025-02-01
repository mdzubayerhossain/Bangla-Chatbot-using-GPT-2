import requests

response = requests.post("http://127.0.0.1:5000/chat", json={"message": "খাবার বড়ি কিভাবে খাব"})
print(response.json())
