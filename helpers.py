import re

def removeHTMLtags(text):
  cleanr = re.compile('<.*?>')
  cleanText = re.sub(cleanr, '', text)
  return cleanText