from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import os
from .forms import FileForm
from .models import File

from django.http import HttpResponse

# Create your views here.

def board_list(request):
    files = File.objects.all()
    return render(request,'file_list.html', {
        'files': files
    })

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

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('file_list')
#     else:
#         form = FileForm()
#     return render(request,'upload_file.html', {
#         'form': form
#     })


# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(os.getcwd())
#             for count, x in enumerate(request.FILES.getlist("files")):
#                 def handle_uploaded_file(file):
#                     with open(os.path.join(os.getcwd(),"media", file.name),'wb+') as destination:
#                         for chuck in file.chucks():
#                             destination.write(chuck)
#                 handle_uploaded_file(x)
#             # form.save()
#             return redirect('file_list')
#     else:
#         form = FileForm()
#         print(os.getcwd())
#     return render(request,'upload_file.html', {
#         'form': form
#     })

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             for count, x in enumerate(request.FILES.getlist("files")):
#                 def handle_uploaded_file(f):
#                     with open(r'C:\VSCODE\django\snapnote_venv\snapnote_django\snapnote\media\files\pdfs\file_' + str(count), 'wb+') as destination:
#                         for chuck in f.chucks():
#                             destination.write(chuck)
#                 handle_uploaded_file(x)
#             # form.save()
#             # return redirect('file_list')
#             return HttpResponse("파일 업로드!")
#     else:
#         form = FileForm()
#     return render(request,'upload_file.html', {
#         'form': form
#     })

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            for count, x in enumerate(request.FILES.getlist("files")):
                def handle_uploaded_file(f):
                    with open('C:\VSCODE\django\snapnote_venv\snapnote_django\snapnote\media\files\pdfs\file_' + str(count), 'wb+') as destination:
                        for chuck in f.chucks():
                            destination.write(chuck)
                handle_uploaded_file(x)
            print(os.getcwd())
            # form.save()
            # return redirect('file_list')
            return HttpResponse("파일 업로드!")
    else:
        form = FileForm()
    return render(request,'upload_file.html', {
        'form': form
    })
    