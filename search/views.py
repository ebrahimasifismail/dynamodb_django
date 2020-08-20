from django.shortcuts import render
from .utils import create_search_request, create_dynamodb, write_to_search_table
# Create your views here.

def search(request):
    if request.method == 'POST':
        query = request.POST['gsearch']
        results = create_search_request(query)

        dynamodb = create_dynamodb()
        data = {"search_id": 0, "search_query": query}
        result = write_to_search_table(dynamodb, data)
        return render(request, 'search_home.html', {"results": results['webPages'], "db_write": result })
    return render(request, 'search_home.html')