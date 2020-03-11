import nltk 
from nltk.corpus import wordnet

import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('http://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text,features="html.parser")
    section = soup.find('section', {'class': 'e1991neq0'})
    if section != None:
        return [span.text for span in section.findAll('span')]
   
#WIP   
def antonyms(term):
    response = requests.get('http://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text,features="html.parser")
    section = soup.find('section', {'class': 'e1991neq0'})
    return [span.text for span in section.findAll('span')]    

def findSynonyms(word):
    synonyms = [] 
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    return(set(synonyms))
        

def findAntonyms(word):
    antonyms = [] 
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
    return(set(antonyms))



