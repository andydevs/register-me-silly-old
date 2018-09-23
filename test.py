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

class TriggerTest(unittest.TestCase):
    """
    Tests Trigger method
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

if __name__ == '__main__':
    unittest.main()
