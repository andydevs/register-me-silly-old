"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""
import unittest
import unittest.mock
import time
import register_me_silly as rms
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
        response = rms.trigger(
            self.test_event,
            key=config.key,
            value1=f'value 1 {time.time()}',
            value2=f'value 2 {time.time()}',
            value3=f'value 3 {time.time()}')
        self.assertEqual(
            response.status_code, 200,
            'Response status code should be 200')
        self.assertEqual(
            response.text,
            f'Congratulations! You\'ve fired the {self.test_event} event',
            'Response text should be correct')

class IsEnrollmentRowTest(unittest.TestCase):
    """
    Tests is_enrollment_row function
    """
    test_url = 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDCyNToJHhmXlAaYXA0sQiEG1ooWtoCQAiXVdwpgAAAA%3D%3D&sp=SA&sp=SANIM&sp=S21401&sp=S212&sp=0'

    def test_is_enrollment_row(self):
        """
        Tests is_enrollment_row method
        """
        soup = BeautifulSoup(get(self.test_url).content, 'html.parser')

        # Get enrollment row
        enrollment_row = soup.find(rms.is_enrollment_row)

        # Run checks
        cells = enrollment_row.find_all('td')
        self.assertEqual(len(cells), 2, 'Row has two cells')
        self.assertEqual(cells[0].get_text(), 'Enroll', 'First cell is title Enroll')

class AvailableClassCheckTest(unittest.TestCase):
    """
    Docstring for AvailableClassCheckTest
    """
    test_id = 'ANIM212'
    test_url = 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDCyNToJHhmXlAaYXA0sQiEG1ooWtoCQAiXVdwpgAAAA%3D%3D&sp=SA&sp=SANIM&sp=S21401&sp=S212&sp=0'

    def test_has_enrollment_available(self):
        """
        Tests has_enrollment_available function
        """
        self.assertTrue(
            rms.has_enrollment_available(self.test_url),
            'Enrollment should be available for this url')

    @unittest.mock.patch('register_me_silly.trigger')
    def test_check_enrollment_for_class(self, mock_trigger):
        """
        Tests check_enrollment_for_class function for available
        """
        rms.check_enrollment_for_class(
            self.test_id,
            self.test_url,
            key=config.key)
        mock_trigger.assert_called_with(
            'class_enroll_available',
            key=config.key,
            value1=self.test_id)

class UnavailableClassCheckTest(unittest.TestCase):
    """
    Docstring for UnavailableClassCheckTest
    """
    test_id = 'ANIM212'
    test_url = 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDCyNToJHhmXlAaYXA0sQiEG1ooWtoCQAiXVdwpgAAAA%3D%3D&sp=SA&sp=SANIM&sp=S23998&sp=S212&sp=0'

    def test_has_enrollment_available(self):
        """
        Tests has_enrollment_available function
        """
        self.assertFalse(
            rms.has_enrollment_available(self.test_url),
            'Enrollment should be unavailable for this url')

    @unittest.mock.patch('register_me_silly.trigger')
    def test_check_enrollment_for_class(self, mock_trigger):
        """
        Tests check_enrollment_for_class function for unavailable
        """
        rms.check_enrollment_for_class(
            self.test_id,
            self.test_url,
            key=config.key)
        mock_trigger.assert_not_called()

if __name__ == '__main__':
    unittest.main()
