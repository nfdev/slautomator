import sys
sys.path.append("/home/hogemin/py_sb/")

from siteclass import *
from slautomator.sitemap import Sitemap

sa = sitea.SiteA("sitea")
sb = siteb.SiteB("siteb")
sc = siteb.SiteB("sitec")
sd = siteb.SiteB("sited")

sitemap = Sitemap("http://google.co.jp")
sitemap.add(sa)
sitemap.add(sb)
sitemap.add(sc)
sitemap.add(sd)
sitemap.link("sitea","siteb")
sitemap.link("siteb","sitea")
sitemap.link("sitea","sitec")
sitemap.link("siteb","sited")
sitemap.set_root("sitea")
print sitemap.search("sitea","siteb")
print sitemap.search("sitea","sitec")
print sitemap.search("sitea","sited")
print sitemap.search("sitec","sitea")
