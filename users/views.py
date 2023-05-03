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
   	    dataToregUser = UsersConfig.objects.filter(email=email).values()
   	    emailTouser = ""
   	    for data in dataToregUser:
   	    	emailTouser = data['email'];
   	    #emailToregUser = UsersConfig.objects.values_list('email', flat=True).distinct()
   	    if emailTouser=="":
   	    	datauser = UsersConfig(email=email,password=password)
   	    	datauser.save()
   	    	request.session['success_message'] = 'You have successfully created account'
   	    	request.session['error'] = False;
   	    	request.session.set_expiry(300)
   	    	return HttpResponseRedirect("/login") 
   	    else:
   	    	request.session['error'] = True;
   	    	request.session['error_message'] = 'You have already account.'
   	    	request.session.set_expiry(300)
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
				request.session['userid'] = ""
				request.session['useremail'] = ""
				request.session['error'] = True;
				request.session['error_message'] = 'Your password not match.'
				return HttpResponseRedirect('/login')
		else:
			request.session['error'] = True;
			request.session['error_message'] = 'You dont have any account.'
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