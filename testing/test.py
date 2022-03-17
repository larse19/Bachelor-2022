import requests

url = "https://at-bachelor.atlassian.net/wiki/rest/api/content/1310721"

payload="{\r\n    \"version\": {\r\n        \"number\": 25,\r\n        \"minorEdit\": true\r\n    },\r\n    \"title\": \"Test page updated from postman again\",\r\n    \"type\": \"page\",\r\n    \"space\": {\r\n        \"id\": 33014,\r\n        \"key\": \"~955037829\",\r\n        \"name\": \"Anders Larsen\"\r\n    },\r\n    \"body\": {\r\n        \"storage\": {\r\n            \"value\": \"<body>\\n<script src='https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js'></script>\\n<div class='mermaid'>\\n graph TD \\n A[Client] --> B[Load Balancer] \\n B --> C[Server01] \\nB --> D[Server02]\\n</div></body>\",\r\n            \"representation\": \"storage\"\r\n        }\r\n    }\r\n}"
headers = {
  'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)