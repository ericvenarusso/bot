from scrap import Scrap
from config import config

class Main:

	def __init__(self):
		self.titles = None
		self.links = None

	def pipeline(self):
		soup_handler = Scrap.get_html(config.SITE+config.PROMOTIONAL_PAGE)

		self.text = Scrap.get_data(soup_handler, 'a', 'thread_title_', text = True)
		self.links = Scrap.get_data(soup_handler, 'a', 'thread_title_', obj = 'href')
		self.links = Scrap.build_link(config.SITE, self.links)

		return dict(zip(self.text, self.links))