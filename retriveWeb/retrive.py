# -*- coding: utf-8 -*-

from retriveWeb import parserExtension
from bs4 import BeautifulSoup
import urllib2
import sys


class retriveWeb():

    def __init__(self, url=None, index=None, path_img=None, path_css=None, path_js=None):
        self.url = url
        self.path_index = index
        self.path_img = path_img
        self.path_js = path_js
        self.path_css = path_css
        self.headers = { 'User-Agent' : 'Mozilla/5.0' }

    def read_index(self, path=None):
        html_index = content_web = None
        try:
            if self.path_index:
                f = open(self.path_index, 'r')
                content_web = f.read()
                f.close
                html_index = BeautifulSoup(content_web, "html5lib")
            elif path:
                req = urllib2.Request(self.url, None, self.headers)
                content_web = urllib2.urlopen(req).read()
                html_index = BeautifulSoup(content_web, "html5lib")
                f = open('{}/index.html'.format(path), 'w')
                f.write(content_web)
                f.close
            else:
                raise Exception('Se esperaba el path del proyecto la ruta del index.html')
        except:
            print "Error:", sys.exc_info()[0]
            raise

        self.retrive_css(index=html_index, path_css=self.path_css)
        self.retrive_js(index=html_index, path_js=self.path_js)
        # self.retrive_img(index=html_index, path_img=self.path_img)
        # self.retrive_htmls(index=html_index, path_img=self.path_img)
        # clean = parserExtension()
        # clean.parser_html(self.path_index)

    def retrive_css(self, index=None, path_css=None):
        """We get like argument a directory where are all files css"""
        content_css = None
        if index:
            for link in index.find_all('link', {'type': 'text/css'}):
                url = link.get('href')
                self._save_files(url=url, path=path_css, extension='css')
        return True

    def retrive_js(self, index=None, path_js=None):
        """We get like argument a directory where are all files js"""
        content_js = None
        if index:
            for link in index.find_all('script', {'type': 'text/javascript'}):
                url = link.get('src')
                if url:
                    self._save_files(url=url, path=path_js, extension='js')
        return True

    def retirve_htmls():
        pass

    def retrive_img(self, index=None, path_img=None):
        """We get like argument a directory where are all files js"""
        content_img = None
        if index:
            for link in index.find_all('img'):
                url = link.get('src')
                if url:
                    self._save_files(url=url, path=path_img)
        return True

    def _get_name_file(self, link=None, extension=None):
        name = None
        _list = link.split('/')
        _list_name = _list[len(_list)-1]
        _list_name = _list_name.split('.')
        if extension == _list_name[1]:
            name = '{}.{}'.format(_list_name[0],_list_name[1])
        return name



    def _save_files(self, url=None, path=None, extension=None):
        if not 'google' in url:
            name_file = self._get_name_file(link=url, extension=extension)
            print('--> Recuperando {}'.format(name_file))
            req = urllib2.Request(url, None, self.headers)
            content = urllib2.urlopen(req).read()
            xfile = open('{}/{}'.format(path,name_file), 'w')
            xfile.write(content)
            xfile.close
        return True