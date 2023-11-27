# calendar_notes_app.py
import PySimpleGUI as sg
from notes_manager import NotesManager

class CalendarNotesApp:
    def __init__(self):
        sg.theme('Default1')
        self.notes_manager = NotesManager()
        self.layout = [
            [sg.Text('Select date:'), sg.CalendarButton('Choose date', target='date')],
            [sg.InputText(key='date', visible=False)],
            [sg.Text('Enter note:')],
            [sg.Multiline(size=(40, 4), key='note')],
            [sg.Button('Save'), sg.Button('Show Notes'), sg.Button('Exit')],
            [sg.Text(size=(40, 5), key='note_display')]
        ]
        self.window = sg.Window('Calendar Notes', self.layout)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
            elif event == 'Save':
                self.save_note()
            elif event == 'Show Notes':
                self.show_notes()

        self.window.close()

    def save_note(self):
        date_str = values['date']
        note = values['note']

        if date_str:
            date = self.notes_manager.parse_date(date_str)
            self.notes_manager.save_note(date, note)
            sg.popup('Note saved!')
        else:
            sg.popup_error('Select a date!')

    def show_notes(self):
        date_str = values['date']
        if date_str:
            date = self.notes_manager.parse_date(date_str)
            notes = self.notes_manager.get_notes_for_date(date)
            self.window['note_display'].update('\n'.join(notes))
        else:
            sg.popup_error('Select a date!')

if __name__ == '__main__':
    app = CalendarNotesApp()
    app.run()
