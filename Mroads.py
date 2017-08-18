import requests 
import re
from bs4 import BeautifulSoup 

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def night_crawler(): 
    url = "http://www.jobs.ac.uk/careers-advice/managing-your-career/1318/what-is-continuing-professional-development-cpd"
    source_code = requests.get(url) #fetching sourcecode. This is similar to VIEW SOURCE option
    plain_text = source_code.text #Reading the text from the source code
    soup = BeautifulSoup(plain_text, "html.parser")
    
    lines = []      
    
    for para in soup.findAll("p") :
        spara = str(para)
        # print(type(spara))
        spara = cleanhtml(spara)
        # print(spara)
        lines.append(spara.split('. '))
    
    
    ans = [sentence for line in lines for sentence in line]
    
   
    for a in ans :
        print(a)
   

night_crawler()       