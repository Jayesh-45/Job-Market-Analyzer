import requests
from bs4 import BeautifulSoup
from jobspy import scrape_jobs

def getHtmlDoc(search_query): 
    # This fuction will return html document collected from web to srapper fuction 
    payload = { 'api_key': '681524e5a46e49fcb69d0fb68a147bfc', 'url': 'https://in.indeed.com/jobs?q='+search_query } 
    html_doc = requests.get('https://api.scraperapi.com/', params=payload).text
    return html_doc

# This function will save the data from dictionary to csv file

def scrape_data(search_query):
    # print("Search query inside scrapper: ", search_query)
    # Call getHtmlDoc here
    html_doc = getHtmlDoc(search_query)  
    #print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    filters = soup.find_all('div', class_="yosegi-FilterPill-dropdownPillContainer")
    filter_dict = {}
    for f in filters:
        filter_name = f.find('div', class_='yosegi-FilterPill-pillLabel').string.strip() 
        if(filter_name == 'Date posted'):
            continue
        list_items=f.find_all('li')
        dict1 = {}
        for li in list_items:
            filter_list_item = li.a.string.strip()
            iop = filter_list_item.index('(') # get index of opening paranthesis
            list_item_name = filter_list_item[:iop-1]
            list_item_value = filter_list_item[iop+1:len(filter_list_item)-1]
            list_item_value = int(list_item_value.replace(',', '')) # convert String value to integer value
            dict1[list_item_name] = list_item_value
        filter_dict[filter_name] = dict1
    # print(filter_dict)
    return filter_dict

def find_jobs(search_query):
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin"],
        search_term=search_query,
        location="India",
        results_wanted=10,
        country_indeed='India'  # only needed for indeed / glassdoor
    )
    return jobs