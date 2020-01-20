import gspread
from random import random
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Brogress-6abff84d908d.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open("testBrogress")
initial = spreadsheet.worksheet('initial')

# Rows and Columns to update are all but the firsts
rtu = len(initial.get_all_values()) - 1
ctu = len(initial.get_all_values()[0]) - 1


# Create a semi-brownian function to change each exercise 5% based on the previous entry
def bronian(origin):
    if random() > 0.5:
        return origin * (1 + random() * 0.05)
    else:
        return origin * (1 - random() * 0.05)

# Update row-by-row
for origin in range(rtu):
    for col in range(ctu):
        initial.update_cell(origin + 1, col + 1, bronian(initial.cell(origin, col + 1,).value))