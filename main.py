import requests
import markdown

URL = "http://localhost:1337/api/articles"

params = {
    "filters[slug][$eq]": "what-s-inside-a-black-hole",
    "populate": "*"
}

response = requests.get(URL, params=params)
article = response.json()["data"][0]

print(article)
# Get the blocks
blocks = article["blocks"]

html_parts = []

for block in blocks:
    if block["__component"] == "shared.rich-text":
        md = block["body"]
        html = markdown.markdown(md)
        html_parts.append(html)

html_content = "\n".join(html_parts)

print(html_content)
