from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#Creating a falsk application instance
app = Flask(__name__)


@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://kandukurisukeerthi.atlassian.net/rest/api/3/issue"
    API_TOKEN = "ATATT3xFfGF0YOKTOLHpEk1kZk6w3n8qYPcWJC_moeBdOJYvPihz8iNJ_ePukeCyWAyqB2UfQNXATdAR84IKQWE-hskQInlIjDLTGoBKzB_pU5LinEu-uhguAxPO3EOaRcxvAWj_xRx_68VGdt8yfDcvXbOtQBC4-ChkjKwZ4S50YYO93MSWgXQ=75C5F160"

    auth = HTTPBasicAuth("kandukurisukeerthi@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First API Jira Ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
        "issuetype": {
        "id": "10006"
        },
        "project": {
        "key": "SK"
        },
        
        "summary": "First API Issue",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run('0.0.0.0', port=5000)