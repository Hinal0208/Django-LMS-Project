from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
User = get_user_model()


def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')



def doLogin(request):
    if request.method == "POST":
       user = EmailBackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('manager_Home')
           elif user_type == '2':
               return redirect('mentor_Home')
           elif user_type == '3':
               return redirect('manager_Home')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('login')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')

# def PROFILE(request):
#     return render(request,'profile.html')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'hinal.panchal82582@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})



