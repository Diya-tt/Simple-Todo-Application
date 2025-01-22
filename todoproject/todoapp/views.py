from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,TemplateView,FormView
from todoapp.forms import UserRegisterForm,UserLoginForm,TodoForm,TodoEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from todoapp.models import TodoModel



# Create your views here.

class Home(TemplateView): 
    template_name='index.html'


class SignInView(CreateView):               #grenericview
    template_name='signin.html'
    form_class=UserLoginForm
    model=User
    def post(self,request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(self.request,"LOGIN SUCCESSFUL")
            return redirect('home_view')
        else:
            messages.warning(self.request,"LOGIN FAILED")
            return redirect('signin_view')
        
class SignUpView(CreateView): # generic method
    template_name='signup.html'
    form_class=UserRegisterForm
    model=User
    # success_url=reverse_lazy('signin_view') #not encrypted 

    def form_valid(self,form):
        User.objects.create_user(**form.cleaned_data )
        messages.success(self.request,"REGISTRATON SUCCESSFUL") #if we want to pass message, we should pass form_valid()
        return redirect('signin_view')
    

    def form_invalid(self,form):
        messages.warning(self.request,"INVALID INPUT")
        return redirect('signup_view')
    
class SignOutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logout Successful")
        return redirect("signin_view")
    

class  TodoCreateView(CreateView):  #generic method
    template_name='create.html'
    form_class=TodoForm
    model=TodoModel
    success_url =reverse_lazy('home_view')  #not encrypted. but no prblm.redirect into this page

    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"Todo added")
        return super().form_valid(form)
    
class TodoListView(ListView):   #generic method 
    template_name='list.html' 
    model=TodoModel
    context_object_name="todos"  #all data of all user

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)
    
class TodoDeleteView(DeleteView): #(here they ask confirmtion) #generic method0
    model=TodoModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('list_view')
    template_name='delete.html'

class TodoEditView(UpdateView):  #generic method
    form_class=TodoEditForm
    template_name='edit.html'
    model=TodoModel
    pk_url_kwarg="id" #-f url le pk instead if id
    success_url=reverse_lazy('list_view')