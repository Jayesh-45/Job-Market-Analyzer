from django.shortcuts import render, HttpResponse 
from .scraper import scrapper
# Create your views here.

# index handles views for '/' url
def index(request):
    search_query = request.GET.get('search_query', '')  # Get the search query from the query parameters
    search_results = scrapper(search_query)
    return render(request, 'home.html', {'search_query': search_query, 'search_results' : search_results})

def about(request):
    return HttpResponse("This is about page.")