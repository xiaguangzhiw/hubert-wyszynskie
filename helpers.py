import re

def removeHTMLtags(text):
  cleanr = re.compile('<.*?>')
  cleanText = re.sub(cleanr, '', text)
  return cleanText

def prepareNotes(notesRaw):
  notes = notesRaw.split('--*/notes-separator/*--')
  notes.pop()
  return notes
  
def getLabel(keepObj, labelName):
  label = keepObj.findLabel(labelName)
  if label is None:
    label = keepObj.createLabel(labelName)
  return label