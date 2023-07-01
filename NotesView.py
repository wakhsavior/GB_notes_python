class NotesView:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NotesView,cls).__new__(cls)
        return cls.instance
    def showNote(self, note):
        if note != 0:
            print(note)
        else:
            print("Note not found.")
    def showAllNotes(self, notes):
        for note in notes:
            print(note)
    def showMessage(self,msg):
        print(msg)