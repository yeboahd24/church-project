# In views.py file within the same directory as models.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from member.forms import MemberForm
from member.models import Group
from django.contrib import messages


@login_required
def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        groups = Group.objects.all()
        context = {"groups": groups, "form": form}

        if form.is_valid():
            member_name = form.cleaned_data["name"]
            if Group.objects.filter(name=member_name).exists():
                messages.error(
                    request, "Member already exists."
                )  # Add error message if member already exists
            else:
                member = form.save()
                messages.success(request, "Member created successfully.")
                return redirect("member:members")
    else:
        form = MemberForm()
        groups = Group.objects.all()
        context = {"groups": groups, "form": form}

    return render(request, "add_member.html", context=context)

