from django.shortcuts import render, HttpResponse 
from .scraper import scrapper
from .plot_generator import *
# Create your views here.

# index handles views for '/' url
def index(request):
    search_query = request.GET.get('search_query', '')  # Get the search query from the query parameters
    search_results = scrapper(search_query)
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
    return render(request, 'home.html', {'search_query': search_query, 'search_results' : search_results})

def about(request):
    return HttpResponse("This is about page.")