# client.py
import requests
import json

API_URL = "http://127.0.0.1:8000/generate-sql"

tenant_id = input("Enter Tenant ID: ").strip()
user_query = input("Enter your question: ").strip()

payload = {"tenant_id": tenant_id, "user_query": user_query}

response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    data = response.json()
    print("\ SQL Generated Successfully!")
    print("\nGenerated SQL:\n", data['generated_sql'])
else:
    print("\n❌ Error:", response.status_code, response.text)
