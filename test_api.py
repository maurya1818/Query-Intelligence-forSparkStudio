import requests
import json

url = "http://127.0.0.1:8000/queries"
payload = {"query": "find battery technology startups in Southeast Asia"}
headers = {"Content-Type": "application/json"}

print("Sending POST request to:", url)
response = requests.post(url, json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response Body:", json.dumps(response.json(), indent=2))

if response.status_code == 201:
    query_id = response.json().get("id")
    print("\nSending GET request to retrieve query:", query_id)
    get_url = f"{url}/{query_id}"
    get_response = requests.get(get_url)
    print("GET Status Code:", get_response.status_code)
    print("GET Response Body:", json.dumps(get_response.json(), indent=2))
