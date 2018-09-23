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
    def test_trigger(self):
        """
        Tests ifttt webhooks trigger method
        """
        response = dshaft.trigger('test_text', key=config.key)
        self.assertEqual(200, response.status_code, 'Response status code should be 200')

if __name__ == '__main__':
    unittest.main()
