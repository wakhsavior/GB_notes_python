import re
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

    def get_string(self, prompt):
        if not isinstance(prompt, str):
            raise TypeError("prompt must be of type str")
        try:
            return input(prompt)
        except EOFError:
            return None

    def get_int(self, prompt):
        while True:
            s = self.get_string(prompt)
            if s is None:
                return None
            if re.search(r"^[+-]?\d+$", s):
                try:
                    return int(s, 10)
                except ValueError:
                    pass