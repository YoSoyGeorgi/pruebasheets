import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Authentication (assuming you have a valid key.json file)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # Use read-only scope
KEY = 'key.json'
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

# Build the Sheets service
service = build('sheets', 'v4', credentials=creds)

# Specify the spreadsheet ID and range
SPREADSHEET_ID = '11ArcnWwiiD0l3WyDGi1EKn12NIb4ppeodq2j56KlOjQ'
range_name = 'Hoja 1!A1:B8'  # Or use a specific cell range if needed

# Get sheet data
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
values = result.get('values', {})

# Handle empty data case gracefully
if not values:
    print('No data found in the specified range.')
else:
    # Convert values to a JSON-friendly list of dictionaries
    json_data = {}
    for row in values:
        # Check if the row has at least two elements before accessing indices
        if len(row) >= 2:
            day = row[0]
            time = row[1]
            json_data[day] = time
        else:
            print(f"Ignoring row {row} as it does not have enough elements.")

# Print or use the JSON-formatted data
print(json.dumps(json_data, indent=4))  # Pretty-printed JSON for readability