from django.shortcuts import render
from django.core.paginator import Paginator
from member.models import Member

from django.shortcuts import redirect


def list_members(request):
    query = request.GET.get("q")
    if query:
        members = Member.objects.filter(name__icontains=query).order_by("id")
    else:
        members = Member.objects.all().order_by("id")

    paginator = Paginator(members, 10)  # Show 10 members per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "query": query}
    return render(request, "members.html", context=context)


def delete_member(request, member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect("member:members")
