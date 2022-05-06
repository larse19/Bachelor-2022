import requests, json
import csv
from requests.auth import HTTPBasicAuth

#token = 'bGFyc2UxOUBzdHVkZW50LnNkdS5kazpRWjE0Q3kyeVJuQURac3hNYTZCcjM1NkQ='

username = 'larse19@student.sdu.dk'
api_token = 'QZ14Cy2yRnADZsxMa6Br356D'
auth = HTTPBasicAuth(username, api_token)

site = 'https://at-bachelor.atlassian.net'

class Page:
    
    def __init__(self, title, url, page_id):
        self.url = url
        self.id = page_id
        self.title = title
        self.level = 0
        self.ancestors = []
        
    def __str__(self):
        return self.title+' - '+self.url

    def __repr__(self):
        return f'\n{self.level} - {self.title}'

def get_pages(space, *args):

    headers = {
        "Content-Type": "application/json"
    }

    pages = []
    cql = f'space = {space} AND type = page'  # or blogpost
    url = site+f'/wiki/rest/api/content/search?cql={cql}&start=0&limit=50&expand=ancestors'

    # Get that passes in the space and expands the ancestors
    r = requests.get(url, headers=headers, auth=auth)
    
    page_list = r.json()['results']
    for page in page_list:
        
        pages.append(page)
    
    is_next_page = True
    
    while is_next_page:
        try:
            next_page = r.json()['_links']['next']
            url = site+next_page
            r = requests.get(url, headers=headers, auth=auth)
            
            page_list = r.json()['results']
            for page in page_list:
                pages.append(page)
        except KeyError:
            is_next_page = False
            
    return pages


def create_page_obj(page):
    title = page['title']
    url = page['_links']['webui']
    page_id = page["id"]
    p = Page(title, url, page_id)
    
    return p


def sort_pages(page_objs):
    # Add pages to a list based on their hierarchy and parent
    sorted_pages = []
    page_levels = max(page.level for page in page_objs)
    for level in range(page_levels + 1):
        if level == 0:
            # First add pages at the root level of the space
            sorted_pages.extend([page for page in page_objs if page.level == 0])

        else:
            # Create list of pages at the current level
            children = [page for page in page_objs if page.level == level]
            # Create a list of parent pages for the children
            parents = [page for page in sorted_pages if page.level == level - 1]
            for page in children:
                for pg in parents:
                    # Check whether the parent ID is in the child's ancestors and put the child after the parent if so.
                    if pg.id in page.ancestors:
                        try:
                            sorted_pages.insert(sorted_pages.index(pg) + 1, page)
                            continue
                        except ValueError:
                            print(pg.title + ' caused an error')
                    else:
                        continue
    for page in page_objs:
        if page not in sorted_pages:
            sorted_pages.append(page)
                        
    return sorted_pages


def create_csv(space, pages):
    page_levels = max(page.level for page in pages)
    with open(f'./{space}_hierarchy.csv', mode='w+') as levels:
        fieldnames = [f'Tree depth {level}' for level in range(page_levels+1)]

        fieldnames.append('URL')

        writer = csv.DictWriter(levels, fieldnames=fieldnames)

        writer.writeheader()
        
        for page in pages:
            link = site + page.url
            row_dict = {f'Tree depth {page.level}': page.title, 'URL': link}
            writer.writerow(row_dict)

def create_hierarchy_audit_csv(space, *args):
    pages = get_pages(space)
    page_objs = []
    for page in pages:
        pg = create_page_obj(page)
        page_objs.append(pg)
        pg.level = len(page['ancestors'])
        ancestors = page['ancestors']
        pg.ancestors = [ancestor['id'] for ancestor in ancestors]


    sorted_pages = sort_pages(page_objs)
    print(sorted_pages)
    create_csv(space, sorted_pages)
    return None