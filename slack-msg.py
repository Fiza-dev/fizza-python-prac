import requests
import json

# Your Slack webhook URL
webhook_url = "https://hooks.slack.com/services/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"

# Simple message
message = {"text": "Hello World"}

# Send the message
response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

# Check if it worked
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
