
from bs4 import BeautifulSoup
import json
import re
import yaml

f = open("src/product/tree.html", "r")

soup = BeautifulSoup(f)

elements = soup.find(name="div", attrs={ "content":"tree"})
jsontree = json.loads(elements.getText())

print(jsontree)
mainElement = jsontree[0]
elements = mainElement['children']

pagelist = []

def extractElements(element, baseroot=""):
    if element is None:
        return
    if isinstance(element, list):
        for i in element:
            extractElements(i, baseroot)
    else:
        href = element['href']
        text = ""
        if "text" in element:
            text = element['text']
        if not href is None:
            pattern = re.compile("mdwiki.html\\#\\!(.*)$")
            m = pattern.match(href)
            if m:
                filename = m.group(1)
                pagelist.append({ text: "src/product/" + filename })
    if "children" in element:
        children = element['children']
        if children is not None:
            extractElements(children)


extractElements(mainElement)

with open("mkdocs.yml","w") as output_file:
    content = {
        "site_name": "APrint Documentation",
        "theme": {
            "name": 'material' },
        #"extra_css": [
        #    "css/extra.css"
        #],
        "plugins": [            "search",
                                {"pdf-export": {"combined": True}}],
        "nav" : pagelist
    }
    output_file.write(yaml.dump(content))

print("Done")