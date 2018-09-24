#!/usr/bin/env python3
"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from register_me_silly import *
from config import *

# Main routine
if __name__ == '__main__':
    run_periodally(interval,
        lambda: check_enrollment_for_all_classes(classes, key))
