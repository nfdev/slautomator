"""
Common Class to define actions for each sites
"""

class WebSite():
    def __init__(self, sname):
        self.sitename = sname

    def checkin(self, wd):
        """
        Check WebDriver is in this site or not
        """
        return True

    def go(self, wd, sname):
        """
        Execute procedure to goto next site "sitename"

        Input:
          wd: WebDriver
          sitename: sitename of next Site Class

        Return:
          next site entity from sitelist
          ex.) return self.sitelist[sitename]
        """
        return False

    def download(self, wd):
        """
        download and rename file

        """
        wd.implicitly_wait(120)
        # click button
        #wait
        fname = ""
        fdir = "" # get from wd. how?
        fname_out = ""
        fdir_out = "" # how to set ?

        while waiting_time < download_timeout:
            time.slppe()
            waiting_time += sleep_unit
            if os.path.exists(fname):
               os.rename(fnae,fname_out)
               return True
        raise Exception("Download Failure!!")

