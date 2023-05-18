import requests

def get_sports_updates():
  response = requests.get("https://api.thesportsdb.com/v1/json/1/all_sports.json")
  data = response.json()
  sports = data["sports"]
  for sport in sports:
    print(sport["name"])

if __name__ == "__main__":
  get_sports_updates()
