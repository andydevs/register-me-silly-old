"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from config import *

header = """
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""

key = input('Enter your api key: ')

with open('config.py', 'w+') as f:
    f.write('"""' + header + '"""\n\n')
    f.write('# IFTTT Maker Key\n')
    f.write('key = \'' + key + '\'\n\n')
    f.write('# Check every interval\n')
    f.write('interval = ' + str(interval) + '\n\n')
    f.write('# Classes to check\n')
    f.write('classes = {\n' \
        + ',\n'.join(
            f"\t'{classid}' : '{webpage}'"
            for classid, webpage
            in classes.items()) \
        + '\n}\n\n')