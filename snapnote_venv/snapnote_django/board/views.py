from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import os
from .forms import FileForm
from .models import File, Attachment

from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.views import View
from .forms import UploadForm
from django.urls import reverse

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
#             for count, x in enumerate(request.FILES.getlist("files")):
#                 def handle_uploaded_file(f):
#                     with open("C:/VSCODE/django/snapnote_venv/snapnote_django/snapnote/media/files/pdfs/file_" + str(count), 'wb+') as destination:
#                         for chuck in f.chucks():
#                             destination.write(chuck)
#                 handle_uploaded_file(x)
#                 form.save()
#             return redirect('file_list')
#             # return HttpResponse("파일 업로드!")
#     else:
#         form = FileForm()
#     return render(request,'upload_file.html', {
#         'form': form
#     })

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             for count, x in enumerate(request.FILES.getlist("pdfs")):
#                 def handle_uploaded_file(f):
#                     with open(os.path.join(os.getcwd(),"media","files","pdfs", f.name), 'wb+') as destination:
#                         for chuck in f.chucks():
#                             destination.write(chuck)
#                 handle_uploaded_file(x)
#                 form.save()
#             # context = {'form': form,}
#             # return redirect('upload_file.html', context)
#             return redirect('file_list')
            
#     else:
#         form = FileForm()
#     return render(request,'upload_file.html', {
#         'form': form
#     })

# def upload_file(request):
#     form = FileForm()
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():



def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            for count, x in enumerate(request.FILES.getlist("files")):
                def handle_uploaded_file(file):
                    with open(os.path.join(os.getcwd(),"media","files","pdfs", file.name), 'wb+') as destination:
                        for chuck in file.chucks():
                            destination.write(chuck)
                handle_uploaded_file(x)
            form.save()
            print(os.path.join(os.getcwd(),"media","files","pdfs"))
            
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request,'upload_file.html', {
        'form': form
    })    

# class UploadView(FormView):
#     template_name = 'upload_file.html'
#     form_class = FileForm
#     success_url = '/done/'
    
#     def form_valid(self, form):
#         for each in form.cleaned_data['files']:
#             File.objects.create(file=each)
#         return super(UploadView, self).form_valid(form)


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

# def upload_file(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             for count, x in enumerate(request.FILES.getlist("files")):
#                 def handle_uploaded_file(f):
#                     with open(Path("C:/VSCODE/django/snapnote_venv/snapnote_django/snapnote/media/files/pdfs") + f.name) , 'wb+') as destination:
#                         for chuck in f.chucks():
#                             destination.write(chuck)
#                 handle_uploaded_file(x)
                
#             return redirect('file_list')
#             # return HttpResponse("파일 업로드!")
#     else:
#         form = FileForm()
#     return render(request,'upload_file.html', {
#         'form': form
#     })

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

# class FileFieldView(FormView):
#         form_class = FileFieldForm

#         def post(self, request, *args, **kwargs):
#             form_class = self.get_form_class()
#             form = self.get_form(form_class)
#             files = request.FILES.getlist('file')
#             if form.is_valid():
#                 for f in files:
#                     with open(os.path.join(os.getcwd(),"media","files","pdfs", f.name), 'wb+') as destination:
#                         for chunk in f.chunks():
#                             destination.write(chunk)

#                 return JsonResponse({'form': True})
#             else:
#                 return JsonResponse({'form': False})

# class BaseView(View):
#     @staticmethod
#     def response(data = {}, message='', status=200):
#         result = {
#             'data': data,
#             'message' : message,
#         }
#         return JsonResponse(result)

# class BasicUploadView(View):
#     def get(self, request):
#         files_list = File.objects.all()
#         return render(self.request, 'index.html' , {'files': files_list})

#     def post(self, request):
#         form = FileForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             file = form.save()
#             data = {'is_valid': True, 'name': file.file.name, 'url': file.file.url}
#         else: 
#             data = {'is_valid':  False}
#         return JsonResponse(data)

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/board/files/'

    def form_valid(self, form):
       
        for each in form.cleaned_data['files']:
            File.objects.create(title=each, pdf=each)  
        return super(UploadView, self).form_valid(form)

    # def get_absolute_url(self):
    #     return redirect('file_list')

    # def get_success_url(self):
    #     return reverse('board/files')    


       

