from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from staff.forms import LoginForm

@require_http_methods(["GET", "POST"])
def church_staff_login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to 'create_members' after successful login
                return HttpResponseRedirect('/members/')
            else:
                # Add an error message if authentication fails
                messages.error(request, 'Authentication failed. Please check your credentials and try again.')
                return HttpResponseRedirect('/login/')
    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form})