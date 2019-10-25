from django import forms
from .models import Hr
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _


class HrForm(forms.ModelForm):
    class Meta:
        model = Hr
        fields = (
            'name',
            'password',
        )
        labels = {
            'name': _('姓名'),
            'password': _('密码'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
