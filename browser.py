from selenium.webdriver import Firefox, FirefoxProfile, Proxy

def get_firefox(profile_config=None):
    if not profile_config:
    profile_config = {
        'security.warn_entering_secure': False,
        'security.warn_entering_weak': False,
        'security.warn_leaving_secure': False,
        'security.warn_leaving_weak': False,
        'security.warn_submit_insecure': False,
        'security.warn_viewing_mixed': False,
        'browser.download.folderList': 1,
        'browser.download.defaultFolder': "",
        'browser.helperApps.neverAsk.saveToDisk', "application/zip,text/csv",
        }

    # Check mime *
    profile = FirefoxProfile()
    for name in profile_config.keys():
        val = profile_config[name]
        profile.set_preference(name,val)

