import os
from posixpath import dirname
import requests
import base64

def parse_mermaid_macros(filename, filetype):
    if(os.path.isdir(filename)):
        filename += "/index_final.md"
    mermaid_diagram_num = 0
    reading_mermaid = False
    graph = ""
    with open(f"{filename}", "r") as infile:
        lines = infile.readlines()
        for line in lines:
            if line.strip("\n") == "```mermaid":
                reading_mermaid = True
                mermaid_diagram_num += 1                
                diagram_file_name = f'{str(filename).replace(".md","-")}{str(mermaid_diagram_num)}.{filetype}'
            if reading_mermaid:
                if(line.strip("\n") != "```mermaid" and line.strip("\n") != "```"):
                    graph += line
                if line.strip("\n") == "```":
                    reading_mermaid = False
                    graphbytes = graph.encode("ascii")
                    graph = ""
                    base64_bytes = base64.b64encode(graphbytes)
                    base64_string = base64_bytes.decode("ascii")
                    url = f'https://mermaid.ink/img/{base64_string}' if filetype == 'png' else f'https://mermaid.ink/svg/{base64_string}'
                    #print(url)
                    response = requests.get(url)
                    if response.status_code == 200:
                        with open(diagram_file_name, 'wb') as imgfile:
                            imgfile.write(response.content)
                    else:
                        print(response.status_code, response.text)

def run(filename, filetype='png'):
    parse_mermaid_macros(filename, filetype)

def traverse(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if(os.path.isdir(f)):
            traverse(f)
        if(f.endswith('.md')):
            print(f)
            run(f)
            run(f, 'svg')

traverse('./Design Diagrams')
#run('./Design Diagrams/pr vs git push.md')
print('Done')
