from django.shortcuts import render
from django.http import HttpResponse

from .forms import ImageForm

# Create your views here.
def hello(request):
    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'homeApp/index.html', {'image':img_obj})
    form = ImageForm()
    return render(request, 'homeApp/index.html', {
        'form':form
    })