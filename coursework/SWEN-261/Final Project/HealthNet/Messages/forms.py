from django import forms
from .models import Message
from django.contrib.auth.models import User
from Profiles.models import userIsAdmin, userIsDoctor, userIsNurse

class MessageForm(forms.ModelForm):
    choices = []
    for user in User.objects.all():
        if (userIsDoctor(user) or userIsNurse(user) or userIsAdmin(user)) and user.is_active:

            choices.append(user.id)


    qset = User.objects.filter(pk__in=choices)

    recipients = forms.ModelChoiceField(queryset=qset)
    text = forms.Textarea
    class Meta:
        model = Message
        fields = ['recipients', 'text']

    def __init__(self, guser, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        choices = []
        for user in User.objects.all():
            if (userIsDoctor(user) or userIsNurse(user) or userIsAdmin(user)) and user.is_active:
                if user != guser:
                    choices.append(user.id)

        qset = User.objects.filter(pk__in=choices)

        self.fields['recipients'].queryset = qset