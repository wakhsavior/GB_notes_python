import re

# Class View uses for present information for user
#
class NotesView:

    # Show one Note
    def showNote(self, note):
        if note != 0:
            print(note)
        else:
            print("Note not found.")
    # show All notes
    def showAllNotes(self, notes):
        for note in notes:
            print(note)
    # Show information message
    def showMessage(self,msg):
        print(msg)
    # Request string
    def get_string(self, prompt):
        if not isinstance(prompt, str):
            raise TypeError("prompt must be of type str")
        try:
            return input(prompt)
        except EOFError:
            return None
    # Request interger
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