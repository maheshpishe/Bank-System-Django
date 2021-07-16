from django import forms
from .models import Employee,Transaction
class Userform(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'

class Transactform(forms.ModelForm):
	class Meta:
		model=Transaction
		fields='__all__'
		