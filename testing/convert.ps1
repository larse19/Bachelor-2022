docker run -it -v ${pwd}:/data minlag/mermaid-cli -i /data/sample_readme.template.md -o /data/sample_readme.png
py .\mermaid_parser.py
pandoc -s sample_readme.md -o sample_readme.html
py .\json_parser_test.py