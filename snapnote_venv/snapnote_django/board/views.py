from django.shortcuts import render

# Create your views here.

def board_list(request):
    return render(request, 'board_list.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #괄호안에 들어가는거는 input으로 전해지는 html 키
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')