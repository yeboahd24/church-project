from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    group_type = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members', blank=True, null=True)

    def __str__(self) -> str:
        return self.name