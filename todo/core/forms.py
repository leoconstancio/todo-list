from django import forms
from .models import Category, Task

class CategoryForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Sport, Work, Study, Health...'}))

	class Meta:
		model = Category
		exclude = ['user']

class TaskForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	description = forms.CharField(required=False, widget=forms.Textarea(
		attrs={
			"class": "form-control",
			"placeholder": "Ex.: Footbal with friends..."
			}))
	date = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}))
	time = forms.TimeField(widget=forms.TextInput(attrs={"class": "form-control", "type": "time"}))
	priority = forms.ChoiceField(required=False, choices=Task.PRIORITY, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = Task
		exclude = ['user']

	def __init__(self, user=None, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		if user is not None:
			self.fields['category'].queryset = Category.objects.filter(user=user)
