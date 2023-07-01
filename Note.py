import datetime

import functions


class Note():
    _curId = 0
    def __init__(self, id, date, title, msg):
        self.id = id
        self.noteTitle = title
        self.noteMsg = msg
        self.noteDate = date

    @staticmethod
    def createNewNote():
        id = Note._curId + 1
        Note._curId += 1
        title = functions.get_string('Enter Title for note: ')
        msg = functions.get_string('Enter Message for note: ')
        noteDate = datetime.datetime.now()
        return Note(id,noteDate,title,msg)

    def getLastId(cls):
        return cls._curId
    def getNoteId(self):
        return self.id
    def getTitle(self):
        return self.noteTitle
    def getMessage(self):
        return self.noteMsg
    def getDate(self):
        time_format = "%Y-%m-%d %H:%M:%S"
        return format(f"{self.noteDate:{time_format}}")

    def __str__(self):
        time_format = "%Y-%m-%d %H:%M:%S"
        return (format(f"=======  ID: {self.id}  =======\n"
                       f"Change date: \t{self.noteDate:{time_format}}\n"
                       f"Title: \t\t\t{self.noteTitle:80}\n"
                       f"Message: \t\t{self.noteMsg:120}\n"
                       f"=========================\n"))