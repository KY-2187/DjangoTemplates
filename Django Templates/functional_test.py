import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_task_in_list(self, task_string):
		task_list = self.browser.find_element_by_id('task_list')
		task_listitems = task_list.find_elements_by_tag_name('li')

		self.assertIn(
			task_string,
			[item.text for item in task_listitems]
		)

	def test_can_start_and_retrieve_a_list(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do', self.browser.title)

	def test_can_create_new_list(self):
		self.browser.get('http://localhost:8000')
		input = self.browser.find_element_by_id('id_new_item')

		input.send_keys('Finish CSCI40 Project')
		input.send_keys(Keys.ENTER)
		time.sleep(3)

		self.check_for_task_in_list('1: Finish CSCI40 Project')

		input.send_keys('Finish watching all the videos')
		input.send_keys(Keys.ENTER)
		time.sleep(3)

		self.check_for_task_in_list('2: Finish watching all the videos')
	
if __name__ == '__main__':
	unittest.main(warnings='ignore')
