import requests
from bs4 import BeautifulSoup
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept':'*/*'}

# # Sulpak
# URL = 'https://www.sulpak.kz/f/smartfoniy'
# HOST = 'https://www.sulpak.kz'
#
# def get_html(url,params = None):
#     r = requests.get(url,headers = HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html,'html.parser')
#     items = soup.find_all('div',class_ = 'product-container-right-side')
#
#     device = []
#
#     for item in items:
#         device.append({
#             'title' : item.find('h3',class_ = 'title').get_text(strip=True),
#             'price' : item.find('div',class_ = 'price').get_text(strip = True),
#             'link' : HOST + item.find('a').get('href')
#         })
#     return device
#
# def parse(URL):
#     html = get_html(URL)
#     if html != None and html.status_code == 200:
#         device = get_content(html.text)
#         print(device)
#     else:
#         print('Error')
#
# parse(URL)



# 2)
# Technodom

# URL = 'https://www.technodom.kz/smartfony-i-gadzhety/smartfony-i-telefony/smartfony/'
# HOST = 'https://www.technodom.kz'
# HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept':'*/*'}
#
# def get_html(url,params = None):
#     r = requests.get(url,headers = HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html,'html.parser')
#     items = soup.find_all('li',class_='ProductCard')
#     # print(items)
#     print(len(items))
#     device = []
#
#     for item in items:
#         device.append({
#             'title' : item.find('h4').get_text(strip=True),
#             'price' : item.find('p',class_ = 'ProductPrice').find('data').get_text(strip = True),
#             'link' : HOST + item.get('href')
#         })
#     return device
#
# def parse(URL):
#     html = get_html(URL)
#     if html != None and html.status_code == 200:
#         device = get_content(html.text)
#         print(device)
#     else:
#         print('Error')
#
# parse(URL)

# 3)
# Shop.kz
#
# URL = 'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/'
# HOST = 'https://shop.kz'
#
# def get_html(url,params = None):
#     r = requests.get(url,headers = HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html,'html.parser')
#     items = soup.find_all('div',class_ = 'bx_catalog_item_container gtm-impression-product')
#
#     device = []
#
#     for item in items:
#         device.append({
#             'title' : item.find('div',class_ = 'bx_catalog_item_title').find('a').get_text(strip=True),
#             'price' : item.find('span',class_ = 'bx-more-price-text').get_text(strip=True),
#             'link' : HOST + item.find('div',class_ = 'bx_catalog_item_title').find('a').get('href')
#         })
#     return device
#
# def parse(URL):
#     html = get_html(URL)
#     if html != None and html.status_code == 200:
#         device = get_content(html.text)
#         print(device)
#     else:
#         print('Error')
#
# parse(URL)



# 4)
# Mechta

URL = 'https://www.mechta.kz/section/smartfony/'
HOST = 'https://www.mechta.kz'

def get_html(url,params = None):
    r = requests.get(url,headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_ = 'bs3 br4px col-6')

    device = []

    for item in items:
        device.append({
            'title' : item.find('div',class_ = 'q-pt-xs q-px-sm text-ts2 text-color2 ellipsis-2-lines').get_text(strip=True),
            'price' : item.find('div',class_ = 'text-ts3 text-bold text-color2').get_text(strip=True),
        })
    return device

def parse(URL):
    html = get_html(URL)
    if html != None and html.status_code == 200:
        device = get_content(html.text)
        print(device)
    else:
        print('Error')

parse(URL)