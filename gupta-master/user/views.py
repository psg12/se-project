
from django.shortcuts import render, redirect
from wallet.models import balance
from .forms import userlogin,UserCreationForm

from django.contrib.auth.decorators import login_required

#profile page
@login_required
def index(request):
    bal = balance.objects.get_or_create(WUser=request.user)
    a=bal

    return render(request, 'registration/home.html', {"balance": a})

#sign up to be overwrite
def Signup(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #a=balance.objects.create(WUser=request.user)
            #a.save()
            return redirect('/user')
    else:
        form = UserCreationForm()


    return render(request, 'registration/signup.html', {'form': form})


#sign in to be overwrite
def Login(request):
    logout(request)
    username = password =  " "
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'registration/login.html')

