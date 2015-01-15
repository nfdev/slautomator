"""
Web Driver Handler, which access frome site to site.
"""

import os.path

class Automator():
    downloaddir = None

    def __init__(self, wd, sitemap):
        """
          wd:   Web Driver
          sitemap: sitemap instance 
        """
        self.wd = wd
        self.sitemap = sitemap
        self.site = sitemap.rootsite
        self.wd.base_url = sitemap.rooturl
        self.site.login(self.wd)

    def go(self, sname):
        """
          sitename: sitename string, which corresponds to 
                    "Site.sitename"
        """
        path = self.sitemap.search(self.site,sname)
        if path:
            for sname in path:
                 self.site.go(self.wd, sname)
                 self.site = self.sitemap.get(sname)
                 if not self.site.checkin(self.wd):
                     pass # Error Handle, jump fail
        else:
            pass # Error Handling, NoSite

    def close(self):
        self.site = self.site.go(self.rootsitename)
        self.site.logout(self.wd)

    def set_downloaddir(self, dname):
        if os.path.isdir(dname):
            self.downloaddir = dname
        else:
            pass # Error Handling + Contatnts Management
