# No parameter set
import helpers
helpers.display('Sample message')

# Parameter set to True
import helpers
helpers.display('Sample message', True)

# Import everything from helpers module
from helpers import *
display('Sample message')

# Importing the display function from helpers module
from helpers import display
display('Sample message')