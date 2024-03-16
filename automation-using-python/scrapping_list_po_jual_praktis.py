import requests
import pandas as pd

list = []
url = "https://api2-lb.jubelio.com/inventory/v2/items/masters/"
for i in range(1, 11):
    querystring = {"page": f"{i}", "page_size": "10",
                   "sort_by": "last_modified", "sort_direction": "DESC", "bundle_filter": "1"}
    headers = {
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlVTRVI6b2ZmaWNlcm9uYm9hcmRpbmdAZ21haWwuY29tOjY3ZGJlN2EwN2M1NzkzZmY4OGExMjA2MjFiZmExMTA5IiwiZXhwIjoxNzA3NjY2NTY2NzI1LCJpc193bXNfbWlncmF0ZWQiOnRydWUsImlhdCI6MTcwNzYyMzM2Nn0.Mh4ME9c8IX-YgSxkwqNvz7pwkp6aLqmjOU7fqVt7B_s',
    }

    r = requests.request("GET", url, headers=headers, params=querystring)
    data = r.json()

    for x in data['data']:
        list.append(x)

df = pd.DataFrame(list)
df.to_csv('list_item_jubelio.csv', index=False)

print(list)
