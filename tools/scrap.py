import re
import requests
from bs4 import BeautifulSoup


class Scrap: 

	def get_html(link: str) -> BeautifulSoup:
		html  = requests.get(link).text
		return BeautifulSoup(html, 'html.parser')

	def get_data(soup_handler: BeautifulSoup, 
				 tag : str, 
				 exp: str,
				 obj: str = None,
				 text: bool = False) -> list:
		if text:
			return [match.text for match in soup_handler.findAll(tag, id=re.compile(exp))]
		else:
			return [match.get(obj) for match in soup_handler.findAll(tag, id=re.compile(exp))]

	def build_link(site, links) -> list:
		return [f'{site}/{link.split("?")[0]}' for link in links]