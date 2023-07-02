import sys
import NotesModel
import NotesView
import NotesPresenter

# Console program for make and use Notes
# Use MVP model
# Main menu use loop

def main(argv):
    print("This is console Notes program.")
# Create model, view, presenter
    model = NotesModel.NotesModel()
    view = NotesView.NotesView()
    presenter = NotesPresenter.NotesPresenter(model, view)
    play = True
    while play:

        answer = presenter.view.get_string("Console Notes:\n"
                                           "1. Show all notes\n"
                                           "2. Add a note\n"
                                           "3. Change a note\n"
                                           "4. Delete a note\n"
                                           "5. Clear all notes\n"
                                           "6. Save notes\n"
                                           "7. Load notes from file\n"
                                           "8. Export notes to file\n"
                                           "0. Exit\n")
        match answer:
            case "1":
                presenter.showAllNotes()
            case "2":
                presenter.addNote()
            case "3":
                presenter.showAllNotes()
                presenter.changeNote(presenter.view.get_int("Enter Note number: "))
            case "4":
                presenter.delNote(presenter.view.get_int("Enter Note number: "))
            case "5":
                presenter.clearAllNotes()
            case "6":
                presenter.saveNotes()
            case "7":
                presenter.loadNotes()
            case "8":
                presenter.exportNotes()
            case "0":
                presenter.exit()
                play = False
            case _:
                print("Try again!\n")


if __name__ == '__main__':
    main(sys.argv)
