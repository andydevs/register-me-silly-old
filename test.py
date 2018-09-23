"""
Drexel Shaft Protection

Prevents your tiny student butthole from being brutally violated by drexel's
aweful course registration system. Repeatedly checks webtms for enrollment
info of courses

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
import unittest
import drexel_shaft_protection as dshaft
import config
from requests import get
from bs4 import BeautifulSoup

class TriggerTest(unittest.TestCase):
    """
    Tests trigger function
    """
    test_event = 'test_text'

    def test_trigger(self):
        """
        Tests ifttt webhooks trigger method
        """
        response = dshaft.trigger(self.test_event, key=config.key)
        self.assertEqual(
            response.status_code, 200,
            'Response status code should be 200')
        self.assertEqual(
            response.text,
            f'Congratulations! You\'ve fired the {self.test_event} event',
            'Response text should be correct')
        print('From test_trigger: Make sure you\'ve recieved a text message!')

class IsEnrollmentRowTest(unittest.TestCase):
    """
    Tests is_enrollment_row function
    """
    test_url = 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SA&sp=SANIM&sp=S13405&sp=S100&sp=0'

    def test_is_enrollment_row(self):
        """
        Tests is_enrollment_row method
        """
        soup = BeautifulSoup(get(self.test_url).content, 'html.parser')

        # Get enrollment row
        enrollment_row = soup.find(dshaft.is_enrollment_row)

        # Run checks
        cells = enrollment_row.find_all('td')
        self.assertEqual(len(cells), 2, 'Row has two cells')
        self.assertEqual(cells[0].get_text(), 'Enroll', 'First cell is title Enroll')


if __name__ == '__main__':
    unittest.main()
