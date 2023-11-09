import requests
from bs4 import BeautifulSoup
# payload = { 'api_key': 'ece642b4297b80c4f2ccfaee72468fef', 'url': 'https://in.indeed.com/jobs?q=google' } 
# html_doc = requests.get('https://api.scraperapi.com/', params=payload).text
# print(r.text)

# This function will save the data from dictionary to csv file

def scrapper(): 
    html_doc = requests.get('https://www.naukri.com/software-development-jobs?k=software%20development').text
    print(html_doc)
    # soup = BeautifulSoup(html_doc, 'html.parser')
    # filters = soup.find_all('div', class_="yosegi-FilterPill-dropdownPillContainer")
    # filter_dict = {}
    # for f in filters:
    #     filter_name = f.find('div', class_='yosegi-FilterPill-pillLabel').string.strip() 
    #     if(filter_name == 'Date posted'):
    #         continue
    #     list_items=f.find_all('li')
    #     dict1 = {}
    #     for li in list_items:
    #         filter_list_item = li.a.string.strip()
    #         iop = filter_list_item.index('(') # get index of opening paranthesis
    #         list_item_name = filter_list_item[:iop-1]
    #         list_item_value = filter_list_item[iop+1:len(filter_list_item)-1]
    #         list_item_value = int(list_item_value.replace(',', '')) # convert String value to integer value
    #         dict1[list_item_name] = list_item_value
    #     filter_dict[filter_name] = dict1
    # print(filter_dict)
    # return filter_dict
scrapper()