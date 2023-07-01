class NotesPresenter():

    def __new__(cls, model, view):
        if not hasattr(cls,'instance'):
            cls.instance = super(NotesPresenter,cls).__new__(cls)
        return cls.instance
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def addNote(self):
        title = self.view.get_string('Enter Title for note: ')
        msg = self.view.get_string('Enter Message for note: ')
        self.model.addNote(title,msg)
    def delNote(self, id):
        result = self.model.delNote(id)
        if result == 0:
            self.view.showMessage("Wrong note number.")
        else:
            self.view.showMessage(format(f"Note === {id} === successfully deleted."))
    def changeNote(self, idNote):
        result = self.model.delNote(idNote)
        if result != 0:
            self.addNote()
        else:
            self.view.showMessage("Wrong note number.")
    def showAllNotes(self):
        notes = self.model.getAllNotes()
        self.view.showAllNotes(notes)
    def clearAllNotes(self):
        items = self.model.getAllNotes()
        itemsId = []
        for item in items:
            itemsId.append(item.getNoteId())
        for idNote in itemsId:
            self.delNote(idNote)
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
        self.clearAllNotes()
        filename = self.view.get_string("Enter filename to load Notes: ")
        self.model.setFileName(filename)
        result = self.model.readNotesFromFile()
        if  result == 0:
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



