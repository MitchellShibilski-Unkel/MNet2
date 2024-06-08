import duckduckgo_search as duck
from googletrans import Translator


class Mnet2:
    def __init__(self, text, lang: str = 'en'):
        self.text: str = ""
        self.lang = lang
        
        if lang != 'en':
            translator = Translator()
            self.text = translator.translate(text, dest=lang).text
        else:
            self.text = text
        
    def search(self, numOfResults: int = 1) -> str:
        search = duck.duckduckgo_search.DDGS().text(self.text, region="us-en", backend="html", max_results=numOfResults)
        results = search[0]['body']
        self.links = search[0]['href']
        self.title = search[0]['title']
        
        if self.lang != 'en':
            translator = Translator()
            results = translator.translate(results, dest=self.lang).text
        
        return results
    
    def webHistory(self, url: str):
        with open("mnet_history.txt", "w") as i:
            i.write(f"{url.encode('utf-32')}\n")
    
    def getTitles(self):
        return self.title
    
    def getSources(self):
        return self.links
    
web = Mnet2("What is the capital of Germany", "en")
search = web.search(1)
web.webHistory(search)