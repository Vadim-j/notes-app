#notes = ["заметка 1","заметка 2"]
import os 
def display_notes(note_list):
    """
    принимает : список заметок 
    показывает список заметок на экране
    """
    os.system("cls")
    print("все заметки:".upper())
    for index , note in enumerate(note_list):
        if index == 0:
            continue
        print(f'({index}) {note}')

def add_note(text,notes):
    """
    добавляет заметки 
    """
    notes.append(text)
    return notes

def save_to_file(file_name,data_list):
    """
    сохраняет заметки
    """
    with open(file_name+".txt","w",encoding="utf-8")as file:
        file.write("/-".join(data_list))


def load_from_file(file_name):
    """
    загружает заметки в файл
    """
    with open(file_name+".txt","r",encoding="utf-8") as file:
        info = file.read().split("/-")
    return info

def delete_note(index,notes):
    del notes[index]
    return notes

def update_note(notes):
    note_index = int(input("введите номер заметки которую хотите отредактировать:"))
    notes[note_index] = input("введите новый текст заметки:")
    return notes