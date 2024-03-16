from django import forms
from .models import Member,Group

    

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone_number', 'email', 'location', 'group_type']

    def __init__(self, *args,**kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['group_type'].queryset = Group.objects.all()  # Set queryset for group_type dropdown

    def save(self, commit=True):
        instance = super(MemberForm, self).save(commit=False)
        if commit:
            instance.save()
            # Access request object here if needed (optional)
            # messages.success(self.request, 'Member created successfully.')  # Add success message
        return instance
