"""
Register Me Silly

Repeatedly checks Drexel's Term Master Schedule for availability of class sections

Author:  Anshul Kharbanda
Created: 9 - 21 - 2018
"""

# IFTTT Maker Key
key = '[your key]'

# Check every interval
interval = 900

# Classes to check
classes = {
	'ECEC471LAB @ W 9:00 AM - 10:50 AM' : 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SE&sp=SECEC&sp=S11502&sp=S471&sp=6',
	'ECEC471LAB @ T 9:00 AM - 10:50 AM' : 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SE&sp=SECEC&sp=S12756&sp=S471&sp=6',
	'ECECT480 @ TR 11:00 AM - 12:20 PM' : 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SE&sp=SECEC&sp=S16389&sp=ST480&sp=6',
	'FMTV115 @ T 9:30 AM - 12:20 PM'    : 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SA&sp=SFMTV&sp=S15258&sp=S115&sp=0',
	'FMTV115 @ T 12:30 PM - 3:20 PM'    : 'https://termmasterschedule.drexel.edu/webtms_du/app?component=courseDetails2&page=CourseList&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDC0NToAa3xJwchcDSxCKgIgVDC11DSwAnUj6JpAAAAA%3D%3D&sp=SA&sp=SFMTV&sp=S16482&sp=S115&sp=0',
}
