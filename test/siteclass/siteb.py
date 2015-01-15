import sys
sys.path.append("/home/hogemin/py_sb/")

from slautomator import website

class SiteB(website.WebSite):
  def go(self, wd, sitename):
      if sitename == "sitea":
          wd.get("http://yahoo.co.jp")
          return True
      else:
          # Error Handling, no site
          return False
