"""
Drexel Shaft Protection

Prevents your tiny student butthole from being brutally violated by drexel's
aweful course registration system. Repeatedly checks webtms for enrollment
info of courses

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from requests import post, get
from bs4 import BeautifulSoup

def has_enrollment_available(webpage):
    """
    Returns true if the webpage has enrollment available

    :param webpage: the webpage of the class to pull from
    """
    # Get soup
    soup = BeautifulSoup(get(webpage).content, 'html.parser')

    def is_enrollment_row(tag):
        """
        Returns true if the tag is the enrollment row

        :param tag: the tag to check

        :return: true if the tag is the enrollment row
        """
        is_tr = tag.name == 'tr'
        cells = tag.find_all('td')
        has_2_cells = len(cells) == 2
        is_enrollment_cell = 'enroll' in cells[0].string.lower()
        return is_tr and has_2_cells and is_enrollment_cell

    # Find enrollment row
    enrollment = soup.find(is_enrollment_row)
    if enrollment:
        estring = enrollment.find_all('td')[1].string.lower()
        return 'closed' in estring
    else:
        return True

def trigger(event, data, key):
    """
    Trigger event on remote server with key

    :param event: event name to trigger
    :param data: the data to pass into the trigger requests
    :param key: the api key

    :return: response
    """
    return post(
        f'https://maker.ifttt.com/trigger/{event}/with/key/{key}',
        data=data)

def enrollment_check_routine_for_class(classid, webpage):
    """
    Checks the enrollment info for the given class

    :param classid: the class id name
    :param webpage: the class webpage url
    """
    print('Checking enrollment for ' + classid + '...')
    if has_enrollment_available(webpage):
        print('ENROLLMENT IS AVAILABLE!!!')
        PRINT('Sending message...')
        trigger('enroll_available', { 'classid': classid })
    else:
        print('Enrollment unavailable...')
