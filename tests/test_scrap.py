import pytest
from scrap import Scrap
import pdb
from bs4 import BeautifulSoup

def test_get_html():
	# Given
	SITE = 'https://www.hardmob.com.br'

	# When
	soup = Scrap.get_html(SITE)

	# Then
	assert type(soup) is type(BeautifulSoup())

def test_get_data():
	# Given
	SITE = 'https://www.hardmob.com.br/forums/407-Promocoes'
	soup = Scrap.get_html(SITE)

	#WHEN
	text = Scrap.get_data(soup, 'a', 'thread_title_', text = True)
	links = Scrap.get_data(soup, 'a', 'thread_title_', obj = 'href')

	#Then
	assert type(text) is list
	assert len(text) > 0

	assert type(links) is list
	assert len(links) > 0

