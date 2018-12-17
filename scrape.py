from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# Instantiate the LINK global variable
LINK = "https://www.google.co.in/search?q="

def create_query(query):
	return LINK + '+'.join(query)

def get_webpage(query):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=query, headers=headers)
	return urlopen(req).read()

def scrape_links(webpage):
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

def display(data):
	for i in data:
		print(i[0], "\n", i[1], "\n", i[2], '\n')

if __name__ == "__main__":
	query = create_query(input().split(" "))
	webpage = get_webpage(query)
	data = scrape_links(webpage)
	display(data)