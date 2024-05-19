#notes = ["заметка 1","заметка 2"]
def display_notes(note_list):
    for note in note_list:
        print(note)


def add_note(text,notes):
    notes.append(text)
    return notes

def save_to_file(file_name,data_list):
    with open(file_name+".txt","w",encoding="utf-8")as file:
        file.write("/-".join(data_list))


def load_from_file(file_name):
    with open(file_name+".txt","r",encoding="utf-8") as file:
        info = file.read().split("/-")
    return info
