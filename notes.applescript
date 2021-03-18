tell application "Notes"
	if folder "Test folder" exists then
		set counter to 1
		set output to ""
		repeat with aNote in notes in folder "Test folder"
			set noteText to (creation date of aNote as string) & "\n"
			set noteText to noteText & (modification date of aNote as string) & "\n"
			set noteText to noteText & (name of aNote as string) & "\n"
			set noteText to noteText & (body of aNote as string) & "\n"
			
			tell application "TextEdit"
				activate
				make new document
				set oldText to text of document 1
				set text of document 1 to oldText & noteText

				close document 1 saving in POSIX file ("/Users/hubertwyszynski/Desktop/Projects/Python/mac-notes-to-g-keep/applescript-output/" & "note-" & counter & ".txt")
			end tell
			set counter to counter + 1
		end repeat
	else
		display dialog "No such folder!"
	end if
end tell
