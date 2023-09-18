from django import forms
from .models import *


class FormaJuice(forms.Form):
    all = Company.objects.all()
    firma = forms.ModelChoiceField(all, required=False)
    # mas = []
    # for a in all:
    #     mas.append((a.id, a.title))
    # print(mas)
    # firma = forms.ChoiceField(choices=tuple(mas), required=False)
    juice = forms.ModelChoiceField(Product.objects.all(), required=False)


class FormaStudents(forms.Form):
    student = forms.ModelChoiceField(Student.objects.all(), required=False)
    course = forms.ModelChoiceField(Course.objects.all(), required=False)

class FormaUser(forms.Form):
    user = forms.ModelChoiceField(User.objects.all(), required=False)

