"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""

# Config file header
config_file_header = """
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""

def write_config_file(key='', interval=1000, classes=[]):
    """
    Docstring for save_config_data
    """
    with open('config.py', 'w+') as f:
        f.write('"""' + config_file_header + '"""\n\n')
        f.write('# IFTTT Maker Key\n')
        f.write('key = \'' + key + '\'\n\n')
        f.write('# Check every interval\n')
        f.write('interval = ' + str(interval) + '\n\n')
        f.write('# Classes to check\n')
        f.write('classes = [\n' \
            + ',\n'.join(
                f"\t('{classid}', '{webpage}')"
                for classid, webpage in classes) \
            + '\n]\n\n')
