# notes_manager.py
import datetime
import os

class NotesManager:
    def parse_date(self, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    def save_note(self, date, note):
        filename = f'notes_{date}.txt'
        with open(filename, 'a') as file:
            file.write(f'{datetime.datetime.now()}: {note}\n')

    def get_notes_for_date(self, date):
        filename = f'notes_{date}.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                notes = file.readlines()
            return notes
        else:
            return ['No notes for this date.']
