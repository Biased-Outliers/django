from django.shortcuts import render
from django.http import HttpResponse

from .forms import ImageForm

# Create your views here.
def hello(request):
    # text = '''<h1>Welcome to Sabi Sands!</h1>'''
    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'homeApp/index.html', {'result':'YES'})
    form = ImageForm()
    return render(request, 'homeApp/index.html', {
        'form':form
    })