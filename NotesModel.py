import Note
import json
from os import path


class NotesModel(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NotesModel, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.file_base = "./notes.json"
        self.saved = True
        self.items = []
        self.readNotesFromFile()

    def loadNote(self, id, title, msg):
        item = Note.Note(id, title, msg)
        self.items.append(item)

    def addNote(self, title, msg):
        item = Note.Note.createNewNote(title, msg)
        self.items.append(item)
        self.saved = False

    def delNote(self, note):
        i = 0
        if (isinstance(note, Note.Note) and self.items.count(note) > 0):
            count = self.items.count(note)
            for i in range(count):
                self.items.remove(note)
                i += 1
                self.saved = False
        elif (isinstance(note, int) and note > 0):
            for item in self.items:
                if item.getNoteId() == note:
                    idNote = self.items.index(self.getNote(note))
                    self.items.pop(idNote)
                    i += 1
                    self.saved = False
        return i

    def getAllNotes(self):
        return self.items

    def getNote(self, idNote):
        for item in self.items:
            if item.getNoteId() == idNote:
                return item
        return 0

    def getNoteId(self, note):
        for item in self.items:
            if item == note:
                return item.getNoteId()
        return 0
    def saveStatus(self):
        return self.saved

    def getFileName(self):
        return self.file_base

    def setFileName(self, filename):
        self.file_base = filename

    def saveNotesToFile(self):
        jsonNotes = []
        for item in self.items:
            tmpDict = {'id': item.getNoteId(),
                       'date': item.getDate(),
                       'Title': item.getTitle(),
                       'Msg': item.getMessage()}
            jsonNotes.append(tmpDict)
        with open(self.getFileName(), "w", encoding="utf-8") as noteFile:
            json.dump(jsonNotes, noteFile)
        return 0

    def readNotesFromFile(self):
        if path.exists(self.getFileName()):
            with open(self.getFileName(), "r", encoding="utf-8") as noteFile:
                jsonNotes = json.load(noteFile)
                for note in jsonNotes:
                    item = Note.Note.loadNote(note['id'],note['date'],note['Title'],note['Msg'])
                    self.items.append(item)
            return 0
        else:
            return 1
