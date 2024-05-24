import duckduckgo_search as duck
from googletrans import Translator


class Mnet2:
    def __init__(self, text, lang: str = 'en'):
        self.text: str = ""
        
        if lang != 'en':
            translator = Translator()
            self.text = translator.translate(text, dest=lang).text
        else:
            self.text = text
        
    def search(self, numOfResults: int):
        search = duck.duckduckgo_search.DDGS().text(self.text, region="us-en", backend="html", max_results=numOfResults)
        results = search[0]['body']
        self.links = search[0]['href']
        self.title = search[0]['title']
        
        return results
    
    def getTitles(self):
        return self.title
    
    def getSources(self):
        return self.links