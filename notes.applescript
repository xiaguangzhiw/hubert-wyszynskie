tell application "Notes"
	if folder "Test folder" exists then
		set notesList to ""
		repeat with aNote in notes in folder "Test folder"
			set currentNote to (name of aNote as string)
      set currentNote to currentNote & "--*/inside-note-separator/*--"
			set currentNote to currentNote & (body of aNote as string)
			
			set notesList to notesList & currentNote
      set notesList to notesList & "--*/notes-separator/*--"
		end repeat
		
		log notesList
	else
		error "Folder not found"
	end if
end tell
