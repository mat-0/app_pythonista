import feedparser
import re

url = "http://feeds.feedburner.com/wordthink/vIYJ"
entries = feedparser.parse(url)["entries"][:1]
for entry in entries:
    output_desc = remove_img_tags(entry['description'])
    output = output_desc.replace("<p>","").replace("</p>","")
    print("latest: ", output)
    
def remove_img_tags(data):
    p = re.compile(r'<img.*?/>')
    return p.sub('', data)
