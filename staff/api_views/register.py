# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from staff.forms import StaffForm

User = get_user_model()

@login_required
@require_http_methods(["GET", "POST"])
def church_staff_view(request):
    if not request.user.is_authenticated or not request.user.church_staff:
        return JsonResponse({"error": "User does not have permission"}, status=403)

    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Add success message
            messages.success(request, 'Staff member added successfully')
            return redirect('member:members')  # Redirect to a success URL
        else:
            # Add error message
            messages.error(request, 'Form submission error. Please correct the errors.')
    else:
        form = StaffForm()

    return render(request, 'signup.html', {'form': form})