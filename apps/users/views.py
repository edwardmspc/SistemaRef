from django.views.generic import TemplateView, DetailView, View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserCreationInviterForm
from django.http import HttpResponseRedirect 
#from django.http import HttpResponseRedirect 
#from django.contrib.auth.models import User
#from django.contrib.auth import login, authenticate, logout
#from .models import CustomUser
from django.contrib.auth import login, authenticate, logout

# Create your views here.
# def CreateUserView(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Loguear
#             # Redirect al panel
#             #return redirect('/signin/')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})

# Create your views here.
# class SignupView(View):

#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             form_user = CustomUserCreationForm(request.POST)
#             if form_user.is_valid():
#                 form_user.save()
#                 return redirect('/signin/')
#             else: 
#                 form = form_user
#         else:
#             form = CustomUserCreationForm()
#         return render(request, 'users/signup.html', {'form': form})

# Create your views here.
class SignupView(View):
    def post(self, request, *args, **kwargs):
        if request.POST['inviter']:
            form = CustomUserCreationInviterForm(request.POST)
        else:
            form = CustomUserCreationForm(request.POST)

#        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomUserCreationForm()
            # Loguear
            # Redirect al panel
            #return redirect('/signin/')
        return render(request, 'users/signup.html', {'form': form})


    def get(self, request, inviter=None, *args, **kwargs):
        if inviter is not None:
            if not request.POST.copy():
                form = CustomUserCreationInviterForm()
                #print request
                return render({'inviter':inviter},'users/signup.html', {'form': form})
            else:
                pass    
                #form = CustomUserCreationInviterForm(testss)
        else:
            form = CustomUserCreationForm()
        return render(request,'users/signup.html', {'form': form})


class SigninView(View):
    def post(self, request, *args, **kwargs):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                  if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/success/")
                  else:
                     return render(request,'/inactivo/')
            else:
               return render(request,'/nousuario/')

    def get(self, request, *args, **kwargs):
        return render(request,'users/signin.html')