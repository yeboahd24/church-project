from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    group_type = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="members", blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

