
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Brogress-6abff84d908d.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open("testBrogress")
initial = spreadsheet.worksheet('initial')

# allrows will be an array of string-arrays representing the data
# The general format is json-like, e.g. "Body Weight: 168.4"
allrows = initial.get_all_values()

# This code block will build the master json object
# The first-level keys are dates which point to 2nd-level objects
# The second-level key-value pairs are exercise or body weight with corresponding numbers
# Example day:
#   "8/26/19": {
#     "Body Weight": " 168.4",
#     "Squat": " 140",
#     "Overhead Press": " 80",
#     "Planks": " 45",
#     "Triceps Press": " 110",
#     "Chest Fly Machine": " 120"
#   }

def objectify_row(dataObject, sheetRow):
    date = sheetRow.pop(0)
    dataObject[date] = {}
    for entry in sheetRow:
        parse = entry.split(":")
        if parse == ['']:  # This is the result when the cell has no entry
            pass
        elif len(parse) == 0 or len(parse) > 2:  # These would result from bad cell data
            pass
        else:
            dataObject[date][parse[0]] = parse[1].strip()


data = {}

for daterow in allrows:
    objectify_row(data, daterow)

print(data)

with open('./datasets/brogress.json', 'w') as db:
    json.dump(data, db)