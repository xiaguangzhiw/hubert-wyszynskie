import osascript
import gkeepapi
import yaml
from helpers import removeHTMLtags

with open(r'credentials.yml') as file:
    credentials = yaml.load(file, Loader=yaml.FullLoader)

applescript = open("notes.applescript","r").read()

code,err,out = osascript.run(applescript)

notesList = out.split("--*/notes-separator/*--")
notesList.pop()

keep = gkeepapi.Keep()
keep.login(credentials['login'], credentials['pass'])

for note in notesList:
  noteContent = note.split("--*/inside-note-separator/*--")
  noteTitle = noteContent[0]
  noteBody = noteContent[1]

  print(noteContent)

  gnote = keep.createNote(noteTitle, removeHTMLtags(noteBody))
  keep.sync()