import osascript

applescript = open("notes.applescript","r").read()

code,err,out = osascript.run(applescript)

# print(code)
# print(err)
# print(out)