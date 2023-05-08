from django.shortcuts import render
from users.models import UsersConfig
from django.http import HttpResponse;
from django.http import HttpResponseRedirect;
from django.contrib import messages
from catalog_settings.models import *
from cart.forms import CartAddProductForm
def reg(request):
	title= {"title":"Registration page"}
	return render(request,"registration.html",title)
# Create your views here.

def regUser(request):
    for key,value in request.POST.items():
    	if request.POST.get(key) == "":
    		return render(request,"registration.html",{'error':True})

    if request.method=="POST":
   	    email = request.POST.get("email")
   	    password = request.POST.get("password")
   	    confirm_password = request.POST.get('confirm_password')
   	    dataToregUser = UsersConfig.objects.filter(email=email).values()
   	    emailTouser = ""
   	    for data in dataToregUser:
   	    	emailTouser = data['email'];
   	    #emailToregUser = UsersConfig.objects.values_list('email', flat=True).distinct()
   	    if emailTouser=="":
   	        if password == confirm_password:
   	            datauser = UsersConfig(email=email,password=password)
   	            datauser.save()
   	            messages.success(request, 'Account created! Welcome to our platform.')
   	            return HttpResponseRedirect("/login")
   	        else:
   	            messages.success(request, 'Confirm your password to proceed, for security purposes.')
   	            return HttpResponseRedirect("/reg")
   	    else:
   	    	messages.success(request, 'Account exists. Please log in to access.')
   	    	return HttpResponseRedirect("/login")


def login(request):
	title= {"title":"Login page"}
	return render(request,"login.html",title)


def loginUser(request):
	if request.method=="POST":
		email = request.POST.get("email")
		dataToregUser = UsersConfig.objects.filter(email=email).values()
		emailTouser = ""
		for data in dataToregUser:
			emailTouser = data['email'];
		if emailTouser!="":
		    emaild = dataToregUser[0]['email']
		    password = request.POST.get("password")
		    passwordToregUser = dataToregUser[0]['password']
		    if password == passwordToregUser:
		        request.session['userid'] = dataToregUser[0]['id']
		        request.session['useremail'] = dataToregUser[0]['email']
		        return HttpResponseRedirect('/home')
		    else:
			    messages.error(request, 'Password error. Please re-enter and try again.')
			    return HttpResponseRedirect('/login')
		else:
			messages.error(request, 'No account found. Please create a new one.')
			return HttpResponseRedirect('/login')


def logout(request):
	request.session['userid'] = 0
	request.session['useremail'] = ""
	return HttpResponseRedirect('/login')

def home(request):
	categories = Category.objects.all()
	prd=products.objects.all()
	cart_product_form= CartAddProductForm()
	return render(request,"after_home.html",{"title":"Home page",'categories':categories,'products':prd,'cart_product_form':cart_product_form})

def testimonial(request):
	title= {"title":"Testimonial"}
	return render(request,"testimonial.html",title)

def product(request):
	title= {"title":"products"}
	return render(request,"products.html",title)

def about(request):
	title= {"title":"about"}
	return render(request,"about.html",title)

def team(request):
	title= {"title":"team"}
	return render(request,"team.html",title)

def faq(request):
	title = {'title':'FAQs'}
	return render(request, 'faq.html',title)

def blog(request):
	title = {'title':'blog'}
	return render(request, 'blog.html',title)


def terms(request):
	title = {'title':'terms'}
	return render(request, 'terms.html',title)

def privacy(request):
	title = {'title':'privacy_policy'}
	return render(request, 'privacy_policy.html',title)