import PySimpleGUI as sg
import datetime
import os

def main():
    sg.theme('Default1')
    layout = [
        [sg.Text('Select date:'), sg.CalendarButton('Choose date', target='date')],
        [sg.InputText(key='date', visible=False)],
        [sg.Text('Enter note:')],
        [sg.Multiline(size=(40, 4), key='note')],
        [sg.Button('Save'), sg.Button('Show Notes'), sg.Button('Exit')],
        [sg.Text(size=(40, 5), key='note_display')]
    ]

    window = sg.Window('Calendar Notes', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Save':
            date_str = values['date']
            note = values['note']
            
            if date_str:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                save_note_to_file(date, note)
                sg.popup('Note saved!')
            else:
                sg.popup_error('Select a date!')
        elif event == 'Show Notes':
            date_str = values['date']
            if date_str:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                notes = get_notes_for_date(date)
                window['note_display'].update('\n'.join(notes))
            else:
                sg.popup_error('Select a date!')

    window.close()

def save_note_to_file(date, note):
    filename = f'notes_{date}.txt'
    with open(filename, 'a') as file:
        file.write(f'{datetime.datetime.now()}: {note}\n')

def get_notes_for_date(date):
    filename = f'notes_{date}.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            notes = file.readlines()
        return notes
    else:
        return ['No notes for this date.']

if __name__ == '__main__':
    main()
