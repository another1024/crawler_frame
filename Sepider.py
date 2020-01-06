from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import quote


class Sepider:
	url = ''
	method = ''
	html = None
	driver = None

	def not_be_use(self):
		return self

	def __init__(self):
		self.driver = webdriver.Chrome(r"C:\Users\21855\Downloads\chromedriver_win32 (1)\chromedriver.exe")

	def set_url(self, url):
		self.url = url

	def resolution_re_text(self, re_text):
		self.not_be_use()
		html = BeautifulSoup(re_text, 'html.parser')
		return html

	def get_request(self, params):

		s = self.url+'?'
		for i in range(0, len(params), 2):
			s += quote(params[i]) + '=' + quote(params[i+1])+'&'

		self.driver.get(s)
		re_text = self.driver.page_source

		self.html = self.resolution_re_text(re_text)
		return re_text

	def search(self, name, param):
		data = self.html.find_all(name=name, attrs=param)
		r = []

		for i in data:
			r.append(i)

		return r

	def close(self):
		self.driver.close()
