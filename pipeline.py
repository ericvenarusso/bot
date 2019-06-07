from tools.scrap import Scrap
from config import config


def pipeline() -> dict:
	soup_handler = Scrap.get_html(config.SITE+config.PROMOTIONAL_PAGE)

	text = Scrap.get_data(soup_handler, 'a', 'thread_title_', text = True)
	links = Scrap.get_data(soup_handler, 'a', 'thread_title_', obj = 'href')
	site_links = Scrap.build_link(config.SITE, links)

	return dict(zip(text, site_links))