import Note
import json
from os import path

# Class Model for Notes, create Notes based class Note
class NotesModel(object):
    def __init__(self):
        self.curId = 0
        self.file_base = "./notes.json"
        self.saved = True
        self.items = []
        self.readNotesFromFile()

# Load Note from data. Set date from data.
    def loadNote(self, id, date, title, msg):
        if self.curId < id:
            self.curId = id
        item = Note.Note.loadNote(id, date, title, msg)
        self.items.append(item)
# Add new Note.
    def addNote(self, id, title, msg):
        lenght = len(self.items)
        if id == 0 or id >= self.curId:
            self.curId += 1
            id = self.curId
        item = Note.Note.createNewNote(id, title, msg)
        self.items.append(item)
        self.saved = False
        if lenght < len(self.items):
            return 0
        else:
            return 1
# Delete Note. Can receive ID or object Note. Check input data before remove.
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
# Get all note and give it to Presenter
    def getAllNotes(self):
        return self.items
# Get one note with ID.
    def getNote(self, idNote):
        for item in self.items:
            if item.getNoteId() == idNote:
                return item
        return 0
# Get note id with object Note
    def getNoteId(self, note):
        for item in self.items:
            if item == note:
                return item.getNoteId()
        return 0
# Get base status change
    def saveStatus(self):
        return self.saved

# Get current base filename
    def getFileName(self):
        return self.file_base

# Adjust new file name
    def setFileName(self, filename):
        self.file_base = filename

# Save current notes to file, use JSON format
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
            self.saved = True
        return 0
# Delete all notes from list and set CurId to 0
    def clearAllNotes(self):
        self.items.clear()
        self.curId = 0
        return self.curId
# Return current ID
    def getCurId(self):
        return self.curId

# Read Notes from file, Use JSON format
    def readNotesFromFile(self):
        if path.exists(self.getFileName()):
            self.clearAllNotes()
            with open(self.getFileName(), "r", encoding="utf-8") as noteFile:
                jsonNotes = json.load(noteFile)
                for note in jsonNotes:
                    item = self.loadNote(note['id'],note['date'],note['Title'],note['Msg'])
            return 0
        else:
            return 1
