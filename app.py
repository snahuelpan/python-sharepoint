import sys 
import requests 
from bs4 import BeautifulSoup 
from shareplum.site import Version 
from shareplum import Site, Office365 
  


authcookie = Office365('https://duhovitcl.sharepoint.com/', username='sebastian.nahuelpan@duhovit.cl', password='19661E$e').GetCookies()
site = Site('https://duhovitcl.sharepoint.com/sites/Simutag2.0', authcookie=authcookie)


new_list = site.List('Pruebas_centinela_BI')
sp_data = new_list.GetListItems(fields=['ID', 'criticidad'])
# print(sp_data)
data = [
            {
                'Title': '5',
                'criticidad': 'baja',
                'nombre_disciplina': 'Operaciones',
                'codigo': 'AS', 
                'nombre_estado': 'Aprobado cierre solicitado', 
                'nametag': 'TERCIARIO', 
                'nombre_planta': 'CHAN-HIDRO', 
                'nombre_area': 'CHANCADO_SEC_TER', 
                'created_datetime': '20-06-2021  11:03:02', 
                'filtro': '20-06-2021', 
                'Tratamiento': 'Pendiente', 
                'Fecha': '20-06-21', 
                'responsable': 'Gonzalo Pizarro Morales', 
                'descripcion': 'prueba python', 
                'Estado de aprobación': '0', 
                'Nivel': '1', 
                'Id. único': '237;#{81A2F230-2A65-4C10-8C9B-C75597596A7A}', 
                'Tipo de elemento': '237;#0', 'Creado':'2021-12-23 18:00', 'Modificado': '2021-12-23 18:00'
                }]
new_list.UpdateListItems(data=data, kind='New') 

sp_data = new_list.GetListItems()
print(sp_data)
# def create_list_items(sp_list, new_items): 
#     """ 
#     Takes a SharePoint List instance and a list of disctoraries. 
#     The keys in the disctorary should match the list column. 
#     """ 
#     if len(new_items) > 0: 
#         try: 
#             sp_list.UpdateListItems(data=new_items, kind='New') 
#         except: 
#             # We should log the specific type of error occurred. 
#             print('Failed to upload new list items: {}'.format(sys.exc_info()[1])) 
  
# # Test the function 
# create_list_items(sp_list, web_list_items) 

# def authenticate(sp_url, sp_site, user_name, password): 
#     """ 
#     Takes a SharePoint url, site url, username and password to access the SharePoint site. 
#     Returns a SharePoint Site instance if passing the authentication, returns None otherwise. 
#     """ 
#     site = None 
#     try: 
#         authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies() 
#         site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=authcookie) 
#     except: 
#         # We should log the specific type of error occurred. 
#         print('Failed to connect to SP site: {}'.format(sys.exc_info()[1])) 
#     return site 
  
# # Test the function 
# sp_site = authenticate(SHAREPOINT_URL,SHAREPOINT_SITE,USERNAME,PASSWORD) 

# def get_sp_list(sp_site, sp_list_name): 
#     """ 
#     Takes a SharePoint Site instance and invoke the "List" method of the instance. 
#     Returns a SharePoint List instance. 
#     """ 
#     sp_list = None 
#     try: 
#         sp_list = sp_site.List(sp_list_name) 
#     except: 
#         # We should log the specific type of error occurred. 
#         print('Failed to connect to SP list: {}'.format(sys.exc_info()[1])) 
#     return sp_list 
  
# # Test the function 
# sp_list = get_sp_list(sp_site, SHAREPOINT_LIST) 