import datetime

#   Class NOTE Include id, title, msg, date
#   For new Note date is current date and time. For load uses data from file
#
class Note():
    def __init__(self, id, date, title, msg):
        self.id = id
        self.noteTitle = title
        self.noteMsg = msg
        self.noteDate = date

    # Static method for create Note. For date uses current date and time
    @staticmethod
    def createNewNote(id, title, msg):
        noteDate = datetime.datetime.now()
        return Note(id, noteDate, title, msg)

    # Static method for create Note from load data.
    @staticmethod
    def loadNote(id, date, title, msg):
        time_format = "%Y-%m-%d %H:%M:%S"
        noteDate = datetime.datetime.strptime(date, time_format)
        return Note(id, noteDate, title, msg)

    def getNoteId(self):
        return self.id

    def getTitle(self):
        return self.noteTitle

    def getMessage(self):
        return self.noteMsg

    # For date uses time format without microseconds
    def getDate(self):
        time_format = "%Y-%m-%d %H:%M:%S"
        return format(f"{self.noteDate:{time_format}}")

    # Overwrite method String for NOTE
    def __str__(self):
        time_format = "%Y-%m-%d %H:%M:%S"
        return (format(f"=======  ID: {self.id}  =======\n"
                       f"Change date: \t{self.noteDate:{time_format}}\n"
                       f"Title: \t\t\t{self.noteTitle:80}\n"
                       f"Message: \t\t{self.noteMsg:120}\n"
                       f"=========================\n"))
