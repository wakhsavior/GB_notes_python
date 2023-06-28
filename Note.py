import datetime

import functions


class Note():
    _curId = 0
    def __init__(self):
        self.id = Note._curId + 1
        Note._curId += 1
        title = functions.inputText('Title')
        msg = functions.inputText('Message')
        self.noteTitle = title
        self.noteMsg = msg
        self.noteDate = datetime.datetime.now()
    def getLastId(cls):
        return cls._curId
    def getNoteId(self):
        return self.id
    def __str__(self):
        time_format = "%Y-%m-%d %H:%M:%S"
        return (format(f"{self.id}: {self.noteDate:{time_format}}\n{self.noteTitle}\n{self.noteMsg}"))