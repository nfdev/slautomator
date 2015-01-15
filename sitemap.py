import sys
sys.path.append("/home/hogemin/py_sb")

from slautomator import website

class Sitemap():
    def __init__(self, url):
        self.sitelist = {}
        self.sitelink = {}
        self.rootsite = None
        self.rooturl = url

    def add(self, site):
        self.sitelist[site.sitename] = site

    def link(self, snamea, snameb):
        if isinstance(snamea, website.WebSite):
            snamea = snamea.sitename
        if isinstance(snameb, website.WebSite):
            snameb = snameb.sitename
        st = self.sitelist
        sk = self.sitelink
        if st.has_key(snamea) and st.has_key(snameb):
            if sk.has_key(snamea):
                sk[snamea].append(snameb)
            else:
                sk[snamea] = [snameb]

    def get(self, sname):
        if self.sitelist.has_key(sname):
            return self.sitelist[sname]
        else:
            return None # Not defined Exception

    def _search(self, snamea, snameb, pathlog):
        sk = self.sitelink
        if not sk.has_key(snamea) or snamea in pathlog:
             return None

        if snameb in sk[snamea]:
             return [snameb]
        else:
           for sname in sk[snamea]:
               path = self._search(sname, snameb, pathlog+[snamea])
               if path:
                   return [sname] + path
           return None

    def search(self, snamea, snameb):
        if isinstance(snamea, website.WebSite):
            snamea = snamea.sitename
        if isinstance(snameb, website.WebSite):
            snameb = snameb.sitename
        return self._search(snamea, snameb, [])

    def set_root(self, sname):
        if isinstance(sname, website.WebSite):
            sname = sname.sitename
        st = self.sitelist
        if not st.has_key(sname):
            pass # Not Defined Exception
        self.rootsite = st[sname]
