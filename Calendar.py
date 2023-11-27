import PySimpleGUI as sg
import datetime

def main():
    sg.theme('Default1')
    layout = [
        [sg.Text('Select date:'), sg.CalendarButton('Choose date', target='date')],
        [sg.InputText(key='date', visible=False)],
        [sg.Text('Enter note:')],
        [sg.Multiline(size=(40, 4), key='note')],
        [sg.Button('Save'), sg.Button('Exit')]
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

    window.close()

def save_note_to_file(date, note):
    filename = f'notes_{date}.txt'
    with open(filename, 'a') as file:
        file.write(f'{datetime.datetime.now()}: {note}\n')

if __name__ == '__main__':
    main()
