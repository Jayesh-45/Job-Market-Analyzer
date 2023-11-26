from django.shortcuts import render, HttpResponse 
from .scraper import *
from .plot_generator import *
from datetime import datetime
from home.models import Contact
# Create your views here.
 
# This function will envoked for the default url
# This page provied the fuctionality to visualize data related to job trends
def index(request):   
    # Get Serach query from the searchbar on the home page
    search_query = request.GET.get('search_query', None) 

    if search_query:  
        # Invoked scrape_data function to gater data related to serach query, this fuction return a dictionary
        search_results = scrape_data(search_query) 

        # Check if the perticular field exit in the result return by the scraper if the field exit generate the respective plot
        if 'Remote' in search_results:
            plot_remote(search_results['Remote'])
        if 'Pay' in search_results:
            plot_salary_dist(search_results['Pay'])
        if 'Education level' in search_results:
            plot_education(search_results['Education level'])
        if 'Location' in search_results:
            plot_locations(search_results['Location'])
        if 'Company' in search_results:
            plot_recruiter(search_results['Company'])
        if 'Job Language' in search_results:
            plot_job_language(search_results['Job Language'])
        if 'Job type' in search_results:
            plot_job_type(search_results['Job type'])
        if 'Programming language' in search_results: 
            plot_skill_cloud(search_results['Programming language']) 
        
        #After generating all the plots render the plots on homepage
        return render(request, 'home.html', {'search_query': search_query, 'search_results' : search_results})
    # If noting the searched by the user then return the default html page
    return render(request, 'home.html')


# This will be used for job portal to find job opening across different companies
def jobportal(request): 
    # Capture search query
    search_query = request.GET.get('search_query', None)
    if search_query:   
        # Invoke scapper to scrap the data
        search_result = find_jobs(search_query).to_dict(orient='records')
        
        # Render the result at front end
        return render(request, 'jobportal.html', {'search_query' : search_query, 'search_result' : search_result})
    # If noting is searched then return default job-portal html page
    return render(request, 'jobportal.html')
def about(request):
    return HttpResponse("This is about page.")

def contact(request):
    if request.method == 'POST': 
        # Get the fields from the from
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')  
        if name != None and email != None and message != None:
            # Create contact instance
            contact = Contact(name=name, email=email, message=message, date=datetime.today())
            # Save the contanct details in the database
            contact.save()
    return render(request, 'contact.html')