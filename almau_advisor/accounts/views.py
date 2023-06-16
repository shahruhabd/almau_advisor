from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Аутентификация через LDAP
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Успешная аутентификация через LDAP
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу
        else:
            # Неверные учетные данные или неудачная аутентификация через LDAP
            return HttpResponse('не вернные данные')
    
    return render(request, 'login.html')



