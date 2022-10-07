import requests
from lxml import html

def get_urls(path):
    file = open(path, 'r')
    content = file.readlines()
    file.close()
    return content

def get_verb_from_web(url, verb):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            }
    
    url = url.replace("ERYKAH", verb)
    response = requests.get(url, headers=headers)
    parser = html.fromstring(response.text)

    result = parser.xpath("(//table[contains(@class, 'table-striped')])[1]//td/text()")
    return result
    

if __name__ == "__main__":
    print(get_verb_from_web('https://pasttenses.com/ERYKAH-past-tense', 'read'))

