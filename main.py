import requests
from bs4 import BeautifulSoup
import json

def getTitle(id=1):
    url = f"https://www.handspeak.com/word/search/index.php?id={id}"
    get_url = requests.get(url)
    get_text = get_url.text
    soup = BeautifulSoup(get_text, "html.parser")

    title = list(soup.select('h1')[0].text.strip().split(" "))[-1].lower()
    return (title, url)

def generateWordsFile(starting=1, maximum=100, filename='words.json'):
    for x in range(starting, maximum + 1):
        title, url = getTitle(x)
        entry = {f"{title}":f"{url}"}
        print(title, x)
        with open('words.json', "r+") as file:
            data = json.load(file)
            data.append(entry)
            #print(data)
            file.seek(0)
            json.dump(data, file)

if __name__ == "__main__":
  generateWordsFile(starting=1, maximum=10464) # Change this to whatever you link
