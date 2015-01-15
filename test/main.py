import sitemap
import pdb

import sys
sys.path.append("/home/hogemin/py_sb")

from slautomator import automator


from selenium import webdriver
wd = webdriver.Firefox()

at = automator.Automator(wd,sitemap.sitemap)
