from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import FileForm
from .models import File
# Create your views here.

def board_list(request):
    return render(request, 'board_list.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #괄호안에 들어가는거는 input으로 전해지는 html 키
        fs = FileSystemStorage()
        # fs.save(uploaded_file.name, uploaded_file) #같은 이름 중복되어도 업로드 가능하게 mulitpleerror 잡음
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def file_list(request):
    files = File.objects.all()
    return render(request,'file_list.html', {
        'files': files
    })

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request,'upload_file.html', {
        'form': form
    })