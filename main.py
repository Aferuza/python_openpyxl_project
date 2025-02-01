import requests

response = requests.get("https://gitlab.com/api/v4/users/aferuza/projects")
print(response.text)

