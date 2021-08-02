from django.shortcuts import render , redirect
from .models import BookOrCourse
from .forms import ContactForm
from .forms import NewUserForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView , ListView
from django.http import HttpResponse


# JUST A SIMPLE RENDERING
def first_page(request) :
    return render(request , 'Menu.html')


# READ ALL THE ITEMS
def rec_list(request) :
    try :
        myobjects = BookOrCourse.objects.all()
    except BookOrCourse.DoesNotExist:
        myobjects = None
    return render(request , 'Books.html' , {'key' : myobjects})
# UPDATE
def rec_update(request , id) :
    if request.method == "POST" :
        my_title = request.POST['title']
        my_producername = request.POST['producername']
        my_level = request.POST['level']
        my_rec_type = request.POST['rec_type']
        my_estimatedtimetocomplete = request.POST['estimatedtimetocomplete']
        # #########################################
        my_object = BookOrCourse.objects.get(id=id)
        # #########################################
        my_object.title = my_title
        my_object.producername = my_producername
        my_object.level = my_level
        my_object.rec_type = my_rec_type
        my_object.estimatedtimetocomplete = my_estimatedtimetocomplete
        my_object.save()
        messages.success(request, 'Item was updated successfully!')
        print("POST in update")
        return redirect('http://DjangoCRUDApp.pythonanywhere.com/booksandcourses/')
    elif request.method == "GET":
        try:
            obj = BookOrCourse.objects.get(id=id)
        except BookOrCourse.DoesNotExist:
            obj = None
        print("GET in update")
        return render(request, 'EditItem.html' , {'key' : obj})

def rec_create(request) :
    if request.method == "POST":
        title = request.POST.get('title',False)
        producername = request.POST.get('producername' , False)
        level = request.POST.get('level' , False)
        rec_type = request.POST.get('rec_type',False)
        estimatedtimetocomplete = request.POST.get('estimatedtimetocomplete' , False)
        myobj = BookOrCourse(title = title , producername = producername , level = level, rec_type = rec_type, estimatedtimetocomplete = estimatedtimetocomplete)

        myobj.save()
        messages.success(request, 'Item was created successfully!')
        print("POST in create")
        return redirect('http://DjangoCRUDApp.pythonanywhere.com/booksandcourses/')
    elif request.method == "GET":
        print("Get in Create")
        return render(request, 'AddItem.html')


def rec_delete(request , id) :
    try:
        obj = BookOrCourse.objects.get(id=id)
        obj.delete()
    except BookOrCourse.DoesNotExist:
        obj = None
    
    messages.error(request, 'Item was deleted successfully!')
    return redirect('http://DjangoCRUDApp.pythonanywhere.com/booksandcourses/')



#   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class SearchResultsView(ListView) :
    model = BookOrCourse
    template_name = 'search_results.html'
    def get_queryset(self) :
        query = self.request.GET.get('q')
        object_list = BookOrCourse.objects.filter(
            Q(title__icontains=query) |
            Q(producername__icontains=query) |
            Q(level__icontains=query) |
            Q(rec_type__icontains=query) |
            Q(estimatedtimetocomplete__icontains=query) 
        )
        return object_list

#   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def contact(request) :
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name' : form.cleaned_data['first_name'],
                'last_name' : form.cleaned_data['last_name'],
                'email_address' : form.cleaned_data['email_address'],
                'message' : form.cleaned_data['message'],
            }

            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found..')
            return redirect('http://DjangoCRUDApp.pythonanywhere.com/')
    form = ContactForm()
    return render(request , "contact.html" , {'form':form})

def register_request(request) :
    if request.method == "POST" :
        form = NewUserForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful..")
            return redirect('http://DjangoCRUDApp.pythonanywhere.com/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request = request, template_name="register.html",context={"register_form":form})



def login_request(request) :
    if request.method == "POST" :
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f" You are now logged in as {username}.")
                return redirect('http://DjangoCRUDApp.pythonanywhere.com/')
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html" , context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('http://DjangoCRUDApp.pythonanywhere.com/')

