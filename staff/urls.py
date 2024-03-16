from staff.api_views.register import church_staff_view
from staff.api_views.login import church_staff_login_view
from django.urls import path


app_name = "staff"

urlpatterns = [
    path("signup/", church_staff_view, name="signup"),
    path("login/", church_staff_login_view, name="login"),
    path("", church_staff_login_view, name="login")

]