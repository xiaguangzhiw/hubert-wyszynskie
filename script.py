import osascript
import gkeepapi
import yaml
from helpers import removeHTMLtags, getLabel, prepareNotes

with open(r'credentials.yml') as file:
  credentials = yaml.load(file, Loader=yaml.FullLoader)

applescript = open('notes.applescript','r').read()

err,code,out = osascript.run(applescript)

if err:
  raise Exception('Something wrong with reading notes')

notesList = prepareNotes(out)

keep = gkeepapi.Keep()
keep.login(credentials['login'], credentials['pass'])

label = getLabel(keep, "From my Mac")

for note in notesList:
  noteContent = note.split("--*/inside-note-separator/*--")
  noteTitle = noteContent[0]
  noteBody = noteContent[1]

  gnote = keep.createNote(noteTitle, removeHTMLtags(noteBody))
  gnote.labels.add(label)

keep.sync()