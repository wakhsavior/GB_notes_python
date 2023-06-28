import sys
import NotesModel

def main(argv):
    NotesModel.Note.addMsg('Title1', 'Msg1')
    NotesModel.Note.addMsg('Title2', 'Msg2')
    NotesModel.Note.addMsg('Title3', 'Msg3')
    NotesModel.Note.addMsg('Title4', 'Msg4')
    NotesModel.Note.addMsg('Title5', 'Msg5')
    NotesModel.Note.addMsg('Title6', 'Msg6')
    NotesModel.Note.addMsg('Title7', 'Msg7')
    NotesModel.Note.addMsg('Title8', 'Msg8')
    for note in NotesModel.Note.items:
        print(note)

    NotesModel.Note.delMsg(3)
    for note in NotesModel.Note.items:
        print(note)
    NotesModel.Note.delMsg(NotesModel.Note.items[5])
    for note in NotesModel.Note.items:
        print(note)
    NotesModel.Note.items[3].changeMsg('Title10', 'Msg10')
    for note in NotesModel.Note.items:
        print(note)
if __name__ == '__main__':
    main(sys.argv)
