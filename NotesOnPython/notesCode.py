import os
import datetime

class Note:
    def __init__(self, id, header, txt):
        self.id = id
        self.header = header
        self.txt = txt
        self.timestamp = datetime.date.today()
    
    def saveToFile(self):
        with open ('notes.txt', mode='a', encoding='utf-8') as f:
            f.write(f"{self.id} {self.timestamp} {self.header} {self.txt} {'\n'}")
    
    @staticmethod
    def loadNotes():
        try:
            notes = []
            with open("notes.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(" ")
                    note = Note(parts[0], " ".join(parts[2:-1]), "")
                    note.timestamp = datetime.datetime.strptime(parts[1], "%Y-%m-%d").date()
                    notes.append(note)
                return notes
        except Exception as e:
            print(e)
            return []
    
    @staticmethod
    def deleteNote(note_id):
        try:
            notes = Note.loadNotes()
            idx = next((i for i, x in enumerate(notes) if x.id == note_id), None)

            if idx != None:
                del notes[idx]
                Note.saveAll(notes)
                print("Note deleted successfully.")
            else:
                print("Note not found.")

        except Exception as e:
            print(e)

    @staticmethod
    def saveAll(notes):
        with open ("notes.txt", "w", encoding='utf-8') as f:
            for note in notes:
                f.write(f"{note.id} {note.timestamp} {note.header} {note.txt} {'\n'}")

    @staticmethod
    def addNote():
        while True:
            id_input = input("Enter a unique ID for the note or press Enter to go back to the previous screen: ")
            if len(id_input) == 0:
                break
            
            if any(char.isdigit() for char in id_input):
                header_input = input("Enter the header of the note: ")
                text_input = input("Enter the body of the note: ")

                new_note = Note(id_input, header_input, text_input)
                new_note.saveToFile()

                print("Note created successfully.")
            else:
                print("Invalid ID format. Please only use numbers.")

    @staticmethod
    def showSortedNotes():
        try:
            notes = Note.loadNotes()

            sorted_notes = sorted(notes, key=lambda n: n.timestamp, reverse=True)

            for note in sorted_notes:
                print(f"\nID: {note.id}\nDate: {note.timestamp}\nHeader: {note.header}\nText:\n{note.txt}\n---")

        except Exception as e:
            print(e)

def mainMenu():
    print("\nWelcome to Notes App\n")
    print("Please select an option:")
    print("  1. Add note")
    print("  2. Delete note")
    print("  3. Show notes sorted by dates")
    print("  0. Exit")

while True:
    mainMenu()
    choice = int(input(">"))

    if choice == 0:
        break
    elif choice == 1:
        Note.addNote()
    elif choice == 2:
        id_to_delete = input("Enter ID of the note to delete: ")
        Note.deleteNote(id_to_delete)
    elif choice == 3:
        Note.showSortedNotes()
    else:
        print("Unknown command. Try again.\n")
