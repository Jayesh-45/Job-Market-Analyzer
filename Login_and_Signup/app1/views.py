from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')


def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your passwords are not same..!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def plot_view(request):
    # Your web scraping and plot generation logic...
    
    education_plot = 'img/plots/education_plot.png'
    job_language_plot = 'img/plots/job_language_plot.png'
    remote_plot = 'img/plots/remote_plot.png'
    salary_dist_plot = 'img/plots/salary_dist_plot.png'
    top_recruiter_plot = 'img/plots/top_recruiter_plot.png'

    return render(request, 'home.html', {
        'education_plot': education_plot,
        'job_language_plot': job_language_plot,
        'remote_plot': remote_plot,
        'salary_dist_plot': salary_dist_plot,
        'top_recruiter_plot': top_recruiter_plot,
    })

# def HomePage(request):
#     return HttpResponse("Home page")