"""
For managing delete and upload data to Google
"""
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet:
    """
    class for managing Google Sheets
        1. upload a csv file to Google Sheets
        2. Delete old sheet in Google Sheets

    Attributes:
        key_file_path (str): a path to Google API service account key file
        spread_sheet_id (str): id of a spreadsheet

    Methods:
        upload_to_sheet(self, csv_file_path: str, g_sheet_name: str) -> None:
            Uploads data from a CSV file to a new sheet.

        delete_sheet(self) -> None:
            Deletes all sheets in the Google Sheets document except a sheet name 'init'.
    """
    def __init__(self) -> None:
        """
        Parameters:
            None
        
        Returns:
            None
        """
        self.key_file_path =  r'source\\spreadsheetAPI\\keys.json'
        self.spread_sheet_id = '1JLlRHiXta8katGaPnHykxxujNtqKwjLKubOcIMjYd_w'

    def upload_to_sheet(self, csv_file_path: str, g_sheet_name: str) -> None:
        """
        Uploading a CSV file to a new sheet in a Google Sheet.

        Parameters:
            csv_file_path (str): Path to the CSV file.
            g_sheet_name (str): Name for the new sheet.
        """
        # Use Service Account credentials for authentication
        credentials = ServiceAccountCredentials.\
            from_json_keyfile_name(self.key_file_path)
        gc = gspread.authorize(credentials)

        # Open the spreadsheet
        spreadsheet = gc.open_by_key(self.spread_sheet_id)

        # Create a new sheet with the provided name
        worksheet = spreadsheet.add_worksheet(title=g_sheet_name,
                                            rows="200",
                                            cols="26"
        )

        # Read CSV data into a list of lists
        with open(csv_file_path, 'r',
                encoding='utf-8-sig') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)

        # Append the data to the new sheet
        worksheet.append_rows(data, value_input_option='RAW')

        print(f"CSV data uploaded to new sheet '{g_sheet_name}'.")

    def delete_sheet(self) -> None:
        """
        Deleting all the old sheets.

        Parameters:
            None
        
        Returns:
            None
        """
        # Use Service Account credentials for authentication
        credentials = ServiceAccountCredentials.\
            from_json_keyfile_name(self.key_file_path)
        gc = gspread.authorize(credentials)

        # Open the spreadsheet
        spreadsheet = gc.open_by_key(self.spread_sheet_id)

        # delete all the sheet except for init sheet
        for sheet in spreadsheet.worksheets():
            if sheet.title == 'init':
                continue
            spreadsheet.del_worksheet(sheet)
        print('\nOld sheet deleted.')

# End of file
