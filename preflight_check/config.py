"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
import yaml

def read_config_file():
    """
    Docstring for read_config_file
    """
    config={}
    with open('config.yaml') as f:
        config = yaml.load(f)
    return config['key'], int(config['interval']), config['classes']

def write_config_file(key='', interval=1000, classes=[]):
    """
    Docstring for write_config_file
    """
    with open('config.yaml', 'w+') as f:
        filedata = yaml.dump({
            'key': key,
            'interval': interval,
            'classes': classes
        }, default_flow_style=False)
        f.write(filedata)
