"""
Drexel Shaft Protection

Prevents your tiny student butthole from being brutally violated by drexel's
aweful course registration system. Repeatedly checks webtms for enrollment
info of courses

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from drexel_shaft_protection import *
from config import *

# Main routine
if __name__ == '__main__':
    run_periodally(interval,
        lambda: check_enrollment_for_all_classes(classes, key))
