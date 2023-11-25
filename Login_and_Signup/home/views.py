from django.shortcuts import render, HttpResponse 
from .scraper import *
from .plot_generator import *
# Create your views here.

# index function handles views for '/' url
def index(request):   
    search_query = request.GET.get('search_query', None)
    print("Search Query: ", search_query)
    if search_query: 
        # Get the search query from the query parameters
        search_results = scrape_data(search_query)
        print("search results" ,search_results)
        #'Remote', 'Pay', 'Job type', 'Education level', 'Location', 'Company', 'Job Language'
        # functions from plot_generator
        # plot_remote, plot_salary_dist, plot_skill_cloud, plot_education, plot_job_type, plot_job_language,
        # plot_locations
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
            print("Programming language...")
            plot_skill_cloud(search_results['Programming language']) 
        return render(request, 'home.html', {'search_query': search_query, 'search_results' : search_results})

    return render(request, 'home.html')

def jobportal(request):
    # print("request.GET", request.GET.get('search_query', None))
    search_query = request.GET.get('search_query', None)
    if search_query:  
        # print(search_data)
        search_result = find_jobs(search_query).to_dict(orient='records')
        # print(type(search_result))   
        return render(request, 'jobportal.html', {'search_query' : search_query, 'search_result' : search_result})
    return render(request, 'jobportal.html')
def about(request):
    return HttpResponse("This is about page.")

def about(request):
    return HttpResponse("This is contact page.")