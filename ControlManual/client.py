from .functions import Functions # Import functions
from .static import Static # Import static

class Client: # Define the client
    def __init__(self): 
        self.path = 'C:/' # Set the default path to 'C:/'
    def getpath(self):
        return self.path


    def changestartingpath(self, args): # Allow someone to change the starting path
        self.path = args

    def instance(self, comm): # The actual control manual instance
        f = Functions() # Initalize functions
        s = Static() # Initalize static

        comm = s.addvars(self, comm)

        comm = comm.split(' ') # Split the command at spaces
        comm.append(' ') # Create a blank one so we don't get index errors
        if comm[0] == '':
            return ''

        if comm[0] == 'compile': # If the command is 'compile'
            slic = s.slicecmd(comm)
            return f.compile(Client, slic + '.cm')

        if comm[0] == 'read':
            slic = s.slicecmd(comm)
            return f.read(slic)

        if comm[0] == 'output': # If the command is 'output'
            return f.output(s.slicecmd(comm))

        if comm[0] == 'get': # If the command is 'get'
           return f.get(s.slicecmd(comm)) # Returns the function 'get' function while passing in the 'slicecmd' function from static
        return s.error('Invalid command.')


