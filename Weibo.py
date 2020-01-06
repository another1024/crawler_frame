from Sepider import Sepider
import time


class Weibo(Sepider):

	def login(self, username, password):
		browser = self.driver
		browser.get('http://weibo.com/login.php')
		browser.implicitly_wait(15)
		browser.find_element_by_xpath('//*[@id="loginname"]').clear()
		browser.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
		browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').clear()
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
		time.sleep(5)
