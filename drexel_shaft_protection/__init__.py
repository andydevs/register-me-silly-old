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
import config

def trigger(event, key='', value1='', value2='', value3=''):
    """
    Trigger event on remote server with key

    :param event: event name to trigger
    :param data: the data to pass into the trigger requests
    :param key: the api key

    :return: response
    """
    return post(
        f'https://maker.ifttt.com/trigger/{event}/with/key/{key}',
        data={'value1': value1, 'value2': value2, 'value3': value3})

def is_enrollment_row(tag):
    """
    True if the tag is an enrollment row

    :param tag: the tag to check

    :return: true if the tag is an enrollment row
    """
    is_tr = tag.name == 'tr'
    cells = tag.find_all('td')
    has_2_cells = len(cells) == 2
    has_enrollment_title = cells[0].get_text() == 'Enroll' \
        if has_2_cells else False
    return is_tr and has_2_cells and has_enrollment_title

def has_enrollment_available(webpage):
    """
    Returns true if the webpage has enrollment available

    :param webpage: the webpage of the class to pull from
    """
    # Get soup
    soup = BeautifulSoup(get(webpage).content, 'html.parser')

    # Return true if enrollment row is not closed
    return soup.find(is_enrollment_row).find_all('td')[1].get_text() != 'CLOSED'

def check_enrollment_for_class(classid, webpage, key):
    """
    Checks enrollment for class

    :param classid: id for class
    :param webpage: webpage for class
    :param key: api key used
    """
    print(f'Checking enrollment for {classid}...')
    if has_enrollment_available(webpage):
        print('OMFG ENROLLMENT AVAILABLE!!!')
        print('Sending a goddamn text message RIGHT NOW!!!')
        trigger('class_enroll_available', key=key, value1=classid)
    else:
        print('Enrollment unavailable...')

def check_enrollment_for_all_classes(classes, key):
    """
    Checks enrollment for all classes

    :param classes: classes to check
    :param key: api key to use for messages
    """
    for classid, webpage in classes.items():
        check_enrollment_for_class(classid, webpage, key)
