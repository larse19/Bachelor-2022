import requests
import upload_attachments

filename = "sample_readme"
reading_mermaid = False
mermaid_diagram_num = 0

url = "https://at-bachelor.atlassian.net/wiki/rest/api/content/1310721/child/attachment"

headers = {
  'Authorization': 'Basic bGFyc2UxOUBzdHVkZW50LnNkdS5kazp6RzFrQk1ick9PUEtZblNSSFA0bTQxNUI=',
  'User-Agent': 'python',
  'X-Atlassian-Token': 'no-check'
}

with open(f"{filename}.template.md", "r") as f:
    lines = f.readlines()
with open(f"{filename}.md", "w") as f:
    for line in lines:
        if line.strip("\n") == "```mermaid":
            reading_mermaid = True
            mermaid_diagram_num += 1
            diagram_name = f"{filename}-{mermaid_diagram_num}"
            f.write(f'<ac:image><ri:attachment ri:filename="{diagram_name}" /></ac:image>')
            response = upload_attachments.upload_new_attachment(diagram_name, f'./{diagram_name}.png')
            print(response)
            if(response.status_code == 400):
                response = upload_attachments.update_attachment_data(diagram_name, f'./{diagram_name}.png')
                print(response)
        if reading_mermaid:
            if line.strip("\n") == "```":
                reading_mermaid = False
        else:
            f.write(line)