from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Snuser
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form}) 


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        email = request.POST.get('email', None)

        res_data = {}

        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력해야합니다'
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            snuser = Snuser( #객체를 만들고
                username = username,
                password = make_password(password), # make_password를 통해 해쉬를 통해 암호화가 된다
                email = email
            ) 

            snuser.save() #객체를 세이브하고 데이터베이스에 생성이 되는지

        return render(request, 'register.html', res_data) #반환하고 싶은 html을 반환, res_data는 에러메시지를 전달하기 위해서 





