import requests # Import the requests library
import traceback # For error handling
from .static import *

class Functions: # Define the class
    def __init__(self):
        self.s = Static()
    def get(self, args): # Define the get function
        try:
            resp = requests.get(args) # Ping the request
            status = resp.status_code # Get the response code
        except:
            status = '404' # If theres an exception, its 404
        try:
            resp = requests.get(args) # Ping the request
            json = resp.json() # Get the json
        except:
            json = 'None' # If theres an exception, theres no JSON
        
        return f'''Response Code: {status}
JSON: {json}''' # Return the status and JSON
    def output(self, text):
        return text
    


    def compile(self, client, file):
        try:
            f = open(file, 'r') # Open the file
        except:
            return self.s.error(f'File "{file}" not found') # Check for an error
        lines = f.readlines() # Get the lines
        resp = '' # Set default response to ''
        c = client() # Define the client
        for i in lines: # Iterate through every line
            resp += c.instance(i) # Add what the compiler would return
        return resp # Return the response
                
    def read(self, file):
        try:
            f = open(file, 'r') # Open the file
        except:
            return self.s.error(f'File "{file}" not found') # Check for an error

        lines = f.readlines() # Get the lines
        resp = ''
        for i in lines: # Iterate through every line
            resp += i
        return resp