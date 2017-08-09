from lxml import html # Needed dep: python-lxml
import requests

page = requests.get('https://www.bitcoin.de/de')
tree = html.fromstring(page.content)
bcoin = tree.xpath('//strong[@id="ticker_price"]/text()')

print ('Current Bitcoin stand in Euro ', bcoin)
