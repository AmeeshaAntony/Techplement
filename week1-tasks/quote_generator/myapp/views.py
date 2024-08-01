import requests
from django.shortcuts import render

def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()
    return None

def search_quotes_by_author(author_name):
    response = requests.get(f'https://api.quotable.io/quotes?author={author_name}')
    if response.status_code == 200:
        return response.json()['results']
    return []

def home(request):
    quote = fetch_random_quote()
    context = {'quote': quote}
    return render(request, 'home.html', context)

def search(request):
    author_name = request.GET.get('author', '')
    quotes = []
    if author_name:
        quotes = search_quotes_by_author(author_name)
    return render(request, 'search.html', {'quotes': quotes, 'author': author_name})
