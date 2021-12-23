import sys 
import requests 
from bs4 import BeautifulSoup 
from shareplum.site import Version 
from shareplum import Site, Office365 
  
AUTHOR_PAGE_URL = 'https://duhovitcl.sharepoint.com/sites/Simutag2.0/SitePages/Home.aspx' 
SHAREPOINT_URL = 'https://trainingcenter2021.sharepoint.com' 
SHAREPOINT_SITE = 'https://duhovitcl.sharepoint.com/sites/Simutag2.0/Lists/Pruebas%20centinela%20BI/' 
SHAREPOINT_LIST = 'MSSQLTips Authors' 
USERNAME = 'sebastian.nahuelpan@duhovit.cl' 
PASSWORD = '19661E$e' 

def authenticate(sp_url, sp_site, user_name, password): 
    """ 
    Takes a SharePoint url, site url, username and password to access the SharePoint site. 
    Returns a SharePoint Site instance if passing the authentication, returns None otherwise. 
    """ 
    site = None 
    try: 
        authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies() 
        site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=authcookie) 
    except: 
        # We should log the specific type of error occurred. 
        print('Failed to connect to SP site: {}'.format(sys.exc_info()[1])) 
    return site 
  
# Test the function 
sp_site = authenticate(SHAREPOINT_URL,SHAREPOINT_SITE,USERNAME,PASSWORD) 

def get_sp_list(sp_site, sp_list_name): 
    """ 
    Takes a SharePoint Site instance and invoke the "List" method of the instance. 
    Returns a SharePoint List instance. 
    """ 
    sp_list = None 
    try: 
        sp_list = sp_site.List(sp_list_name) 
    except: 
        # We should log the specific type of error occurred. 
        print('Failed to connect to SP list: {}'.format(sys.exc_info()[1])) 
    return sp_list 
  
# Test the function 
sp_list = get_sp_list(sp_site, SHAREPOINT_LIST) 