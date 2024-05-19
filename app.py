from library import *
save_to_file("save",["a","!","i"])
notes = load_from_file("save")
notes = add_note("заметка 3",notes)
display_notes(notes)  
save_to_file("save",notes)