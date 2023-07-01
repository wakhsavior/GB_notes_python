import functions
import NotesModel
class NotesPresenter():

    def __new__(cls, model, view):
        if not hasattr(cls,'instance'):
            cls.instance = super(NotesPresenter,cls).__new__(cls)
        return cls.instance
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def addNote(self):
        self.model.addNote()
    def delNote(self, id):
        result = self.model.delNote(id)
        if result == 0:
            self.view.showMessage("Wrong note number.")
        else:
            self.view.showMessage(format(f"Note === {id} === successfully deleted."))
    def changeNote(self, idNote):
        result = self.model.delNote(idNote)
        if result != 0:
            self.model.addNote()
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



