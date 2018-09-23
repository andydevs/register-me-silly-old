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

def is_enrollment_row(tag):
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

def trigger(event, data={}, key=''):
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
