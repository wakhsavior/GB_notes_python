# Class Presenter uses between User View and Model
class NotesPresenter():

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addNote(self):
        id = 0
        title = self.view.get_string('Enter Title for note: ')
        msg = self.view.get_string('Enter Message for note: ')
        result = self.model.addNote(id, title, msg)
        if result == 0:
            self.view.showMessage("Note successfully added.")

    def delNote(self, id):
        result = self.model.delNote(id)
        if result == 0:
            self.view.showMessage("Wrong note number.")
        else:
            self.view.showMessage(format(f"Note === {id} === successfully deleted."))

    def changeNote(self, idNote):
        result = self.model.delNote(idNote)
        if result != 0:
            title = self.view.get_string('Enter Title for note: ')
            msg = self.view.get_string('Enter Message for note: ')
            self.model.addNote(idNote, title, msg)
        else:
            self.view.showMessage("Wrong note number.")

    def showAllNotes(self):
        notes = self.model.getAllNotes()
        self.view.showAllNotes(notes)

    def clearAllNotes(self):
        if self.model.clearAllNotes() == 0:
            self.view.showMessage("All Notes succesfully deleted.")

    def showNote(self, id):
        self.view.showNote(self.model.getNote(id))

    def exportNotes(self):
        filename = self.view.get_string("Enter filename to export Notes: ")
        self.model.setFileName(filename)
        result = self.model.saveNotesToFile()
        if result == 0:
            self.view.showMessage(format(f'Notes succesfully saved to {self.model.getFileName()}.'))

    def saveNotes(self):
        result = self.model.saveNotesToFile()
        if result == 0:
            self.view.showMessage(format(f'Notes succesfully saved to {self.model.getFileName()}.'))

    def loadNotes(self):
        filename = self.view.get_string("Enter filename to load Notes: ")
        self.model.setFileName(filename)
        result = self.model.readNotesFromFile()
        if result == 0:
            self.view.showMessage(format(f'File {filename} succesfully loaded.'))
        elif result == 1:
            self.view.showMessage(format(f'File {filename} not found.'))

    def exit(self):
        if not self.model.saveStatus():
            self.view.showMessage("You have unsaved Notes. Would you like to save it?")
            cont = True
            while cont:
                answer = self.view.get_string('[y/n]').lower()
                if answer == 'y':
                    self.saveNotes()
                    cont = False
                elif answer == 'n':
                    cont = False
