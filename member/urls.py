from member.api_views.add_member import create_member
from member.api_views.members import list_members, delete_member

from django.urls import path


app_name = "member"

urlpatterns = [
    path("add-member/", create_member, name="add_member"),
    path("members/", list_members, name="members"),
    path("delete-member/<int:member_id>/", delete_member, name="delete_member"),
]

