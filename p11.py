from bs4 import BeautifulSoup
import requests

url = 'https://jenkins.io/pipeline/getting-started-pipelines/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# removes a tag or string from the tree. It returns the tag or string that was extracted, this will remove all style and script
for tag in soup(["script", "style"]):
    print(tag.extract()) 

# get text
text = soup.get_text()
print(text.splitlines())

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)