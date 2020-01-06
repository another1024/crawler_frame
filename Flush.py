

class Flush:

	def not_be_use(self):
		return self

	def get_text(self, html_list):
		self.not_be_use()
		r = []

		for i in html_list:
			tmpr = []
			for string in i.strings:
				tmpr.append(repr(string))

			r.append(tmpr)
		return r

	def get_child(self, html_list, name):
		self.not_be_use()
		r = []
		for i in html_list:

			s = i.get(name)
			if s:
				r.append(s)

			return r
