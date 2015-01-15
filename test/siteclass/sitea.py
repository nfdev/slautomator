import sys
sys.path.append("/home/hogemin/py_sb/")

from slautomator import website

class SiteA(website.WebSite):
  def go(self, wd, sitename):
      if sitename == "siteb":
          wd.get("http://google.co.jp")
          return True
      else:
          # Error Handling, no site
          return False
