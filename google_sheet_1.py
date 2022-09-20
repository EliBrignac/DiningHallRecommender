
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sheet_data.json', scope)


# authorize the clientsheet
client = gspread.authorize(creds)


# get the instance of the Spreadsheet
sheet = client.open('UD Dining Preferences (Responses) 2')


# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


# Write in the same way as "get_all_records"
initial_records_data = sheet_instance.get_all_values()


def make_record_template():
    '''
    This makes the Record_template. This is a template that is used
    to make the rest of the records

    args: None

    returns: a dictionary where the keys are the first row in the data,
                and all keys are mapped to an empty string ''
    '''
    Record_template = {}
    for name in initial_records_data[0]:
        Record_template[name] = ''
    return Record_template

def make_record(record):
    '''
    This takes the data from the google sheet and properly displays it

    args:
        record: a list of the responses from the google sheet
                (aka. each row of the google sheet)

    returns:
        new_record: a new record that is a dictionary with each google form question
                    mapped to the records data points.
    '''
    new_record = make_record_template()
    for value,key in zip(record, initial_records_data[0]):
        if new_record[key] == '':
            new_record[key] = value
    return new_record


def correct_initial_records_data():
    '''
    This function cleans up the initial data from the google sheet
    and makes it much easier to use

    args:
        None

    returns:
        corrected_data) A list of dictionaries of all the responses
    '''
    corrected_data = []
    for i in range(1, len(initial_records_data)):
        record = initial_records_data[i]
        corrected_data.append(make_record(record))
    return corrected_data

records_data = correct_initial_records_data()


