import json
import requests
from dateutil.parser import parse

user = "CKtrace"
endpoint = f"https://api.github.com/users/{user}/repos"

repos = json.loads(requests.get(endpoint).text)

mk_dates = [parse(repo["created_at"] for repo in repos)]
up_dates = [parse(repo["updated_at"] for repo in repos)]
