from library import *
import os 
#options = ["an!","aq!","as!","ad!","ar!","au!"]
if os.path.isfile("save.txt"):
    notes = load_from_file("save")
else:
    notes = []

user_input = ""
while user_input!="aq!":
    user_input = input("введите:\nan!-добавить новую заметку\naq!-выход из программы\nar!-удалить заметку\n->".lower())
    if user_input == "an!":
        os.system("cls")
        user_input= input("введите текст новой заметки:\n".lower())
        notes = add_note(user_input,notes)
    elif user_input == "ad!":
      display_notes(notes)    
    elif user_input == "as!":
        save_to_file("save",notes)
        print("заметки сохранены успешно")
    elif user_input == "ar!":
        user_input = int(input("введите номер заметки которую хотите удалить:".lower()))
        notes = delete_note(user_input,notes)
    elif user_input == "au!":
        notes = update_note(notes)
    else:
        print("пожалуйста введите что нибудь из допустимых опций")
save_to_file("save",notes)
    