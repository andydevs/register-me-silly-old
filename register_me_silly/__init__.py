"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
from requests import post, get
from bs4 import BeautifulSoup

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
    try:

        # Get soup
        soup = BeautifulSoup(get(webpage).content, 'html.parser')

        # Return true if enrollment row is not closed
        return soup.find(is_enrollment_row).find_all('td')[1].get_text() != 'CLOSED'

    # Retrn false if anything
    except Exception as e:
        return False

def check_enrollment_for_class(classid, url, key):
    """
    Checks enrollment for class

    :param classid: id for class
    :param url: url for class
    :param key: api key used
    """
    if has_enrollment_available(url):
        trigger('class_enroll_available',
            key=key,
            value1=classid)

def check_enrollment_for_all_classes(classes, key):
    """
    Checks enrollment for all classes

    :param classes: classes to check
    :param key: api key to use for messages
    """
    for klass in classes:
        check_enrollment_for_class(
            classid=klass['classid'],
            url=klass['url'],
            key=key)
