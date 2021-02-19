import requests # Import the requests library

class Static: # Define the static class
    def slicecmd(self, comm): # Create the slicecmd function
        cmd = ''
        for i in comm[1:]: # Iterate through everything that isn't the original command
            if not i == ' ': # If it isn't the final object
                if not comm[-2] == i:
                    cmd += i + ' ' # Add ' ' to it
                else: # If the if above was false, don't add a space
                    cmd += i
        return cmd # Return the sliced command args

    def api(self, url):
        try:
            resp = requests.get(f'https://api.controlmanual.xyz/{url}') # Get the API url
        except:
            return "Failed" # If theres an exception, the API is down. Returns failed
        
        return resp.json() # Else, return the JSON

    def error(self, err): # Error maker
        return f'ERROR: {err}' # Return the error

    def addvars(self, client, comm): # Function that replaces strings of text with variables
        comm = comm.replace('cm/path', client.path) # Add path
        comm = comm.replace('cm/linebreak', '\n')
        return comm # Return the modified comm