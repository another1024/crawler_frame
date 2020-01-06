from Weibo import Weibo
from Flush import Flush


class Main:

	def not_be_use(self):
		return self

	def __init__(self):
		return

	def work(self):
		self.not_be_use()
		weibo = Weibo()
		weibo.set_url('https://s.weibo.com/weibo')

		flush = Flush()
		weibo.get_request(['q', 'asd', 'page', '1'])
		li = weibo.search('p', {'class': 'txt'})
		print(flush.get_child(li, 'herf'))
		print(flush.get_text(li))

		'''
		pape = 0
		pape_tmp = weibo.search('ul.s-scroll')[0]
		while pape_tmp.find('<li>') != -1:
			pape_tmp = pape_tmp[pape_tmp.find('<li>')+1:]
			pape += 1
		print(pape)
		for i in range(pape):
			weibo.get_request(['q', 'asd', 'page', str(i)])
			print(flush.flush(weibo.search('p.txt')))
		'''
		return


if __name__ == "__main__":
	m = Main()
	m.work()
