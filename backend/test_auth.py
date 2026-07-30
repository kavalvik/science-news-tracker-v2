import requests

url = "http://127.0.0.1:8000/api/chat/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg1NDQxNTIzLCJpYXQiOjE3ODU0NDEyMjMsImp0aSI6IjUyZWRmMDgxYmY3NzQzYWZiNzdiNDVlOTlkNmU5ZTY5IiwidXNlcl9pZCI6IjIifQ.SofiH7V_LXquZYLzk4YuEYGlymuB7YvkHvDX0Bo7-9E"
data = {"question": "Что такое квантовый компьютер?"}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())