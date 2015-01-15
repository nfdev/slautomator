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

    def login(self, wd):
        """
        Login Procedule to Enter Site Group
        """
        return True

    def logout(self, wd):
        """
        Logout Procedule to Enter Site Group
        """
        return True
