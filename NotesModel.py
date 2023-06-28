import Note

class NotesModel(object):


    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(NotesModel,cls).__new__(cls)
            items = []
        return cls.instance
    def addMsg(self):
        item = Note()
        self.items.append(item)
    def delMsg(self, note):
        print(type(note))
        i = 0
        if (isinstance(note,Note) and self.items.count(note) > 0):
            count = self.items.count(note)
            for i in range(count):
                self.items.remove(note)
                i += 1
        elif (isinstance(note,int) and note > 0 and note <= len(self.items)):
            for item in self.items:
                if item.getNoteId == note:
                    self.items.pop(note)
                    i += 1
        return i

    def changeMsg(self, id):
        self.delMsg(id)
        self.addMsg()

    def getAllNotes(self):
        return self.items
    def getNote(self,id):
        for item in self.items:
            if item.getNoteId == id:
                return item
        return Note

