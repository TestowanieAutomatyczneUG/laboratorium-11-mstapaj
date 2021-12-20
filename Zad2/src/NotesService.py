from src.NotesStorage import NotesStorage


class NotesService:
    def __init__(self):
        self.notes = NotesStorage()

    def add(self, note):
        return self.notes.add(note)

    def averageOf(self, name):
        notes = self.notes.getAllNotesOf(name)
        if len(notes) == 0:
            return 0
        summary = 0
        for i in notes:
            summary += i.note
        return round(summary / len(notes), 2)

    def clear(self):
        return self.notes.clear()
