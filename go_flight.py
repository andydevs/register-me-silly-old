#!/usr/bin/env python3
"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from register_me_silly import check_enrollment_for_all_classes
from time import sleep
from yaml import load as load_yaml

def run_periodally(interval, func):
    """
    Runs the given function periodically every interval

    :param interval: the interval to run by
    :param func: the function to run
    """
    while True:
        func()
        sleep(interval)

# Main routine
if __name__ == '__main__':
    config = {}
    with open('config.yaml') as f:
        config = load_yaml(f)
    classes = config['classes']
    key = config['key']
    interval = int(config['interval'])
    run_periodally(interval,
        lambda: check_enrollment_for_all_classes(classes, key))
