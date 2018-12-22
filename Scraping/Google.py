from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class Google:
	# Instantiate the self.LINK global variable
	def __init__(self):
		self.LINK = "https://www.google.co.in/search?q="

	def __create_query(self, query):
		return self.LINK + '+'.join(query)

	def __get_webpage(self, query):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
		req = Request(url=query, headers=headers)
		return urlopen(req).read()

	def __scrape_links(self, webpage):
		bsObj = BeautifulSoup(webpage, "html.parser")
		div = bsObj.find_all('div', {'id':'res'})
		# divs = divs.find('div', {'id':'search'})
		divs = div[0].find('div', {'id':'search'}).find_all('div', {'class':'bkWMgd'})
		info = []
		for element in divs:
			try:
				data = element.find('div', {'class':'srg'}).find_all('div', {'class':'g'})
				for i in data:
					total = i.find('div').find('div', {'class':'rc'})
					temp = total.find('div', {'class': 'r'}).find_all('a')
					s = total.find('div', {'class': 's'})
					paras = s.find('div').find('span', {'class':'st'})
					for j in temp:
						info.append((j['href'], j.find('h3'), paras.text))
			except Exception as e:
				pass

		final = []
		for i in info:
			if i[0] != '#' and i[1] != None:
				final.append((i[1].text, i[0], i[2]))

		return final

	def __display(self, data):
		toBeSent = {}
		toBeSent['results'] = []
		for i in data:
			toBeSent['results'].append({
				'title':i[0],
				'link':i[1],
				'description':i[2]			
			})

		return toBeSent

	def scrape(self, query):
		query = self.__create_query(query.split(" "))
		webpage = self.__get_webpage(query)
		data = self.__scrape_links(webpage)
		return self.__display(data)