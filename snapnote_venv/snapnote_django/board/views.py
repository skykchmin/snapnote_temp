from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def board_list(request):
    return render(request, 'board_list.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #괄호안에 들어가는거는 input으로 전해지는 html 키
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file) #같은 이름 중복되어도 업로드 가능하게 mulitpleerror 잡음
    return render(request, 'upload.html')