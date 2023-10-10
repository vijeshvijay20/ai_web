from django.shortcuts import render

def index_view(request):
    # Your view logic here
    return render(request, 'web_page/index.html')
