import requests
import json

#Covid Account
url = 'https://hooks.slack.com/services/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'
message = {'text': 'Finished Execution'}
response = requests.post(url, data = json.dumps(message))
print(response)
