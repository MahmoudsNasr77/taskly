from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
 
from django.contrib.auth.models import User
from django import forms
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter task details'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        label="Username",
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        }),
        label="Email Address",
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label="Password",
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        }),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if username.isdigit():
            raise forms.ValidationError("Username must not be all digits")
        if username.isupper():
            raise forms.ValidationError("Username must not be all uppercase")
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")   
        return email
    def clean_password1(self):
        password1=self.cleaned_data['password1']
        if len(password1)<8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        if password1.isdigit():
            raise forms.ValidationError("Password must not be all digits")
        if password1.isalpha():
            raise forms.ValidationError("Password must not be all alphabets")
        if password1.isupper():
            raise forms.ValidationError("Password must not be all uppercase") 
        if password1.islower():
            raise forms.ValidationError("Password must not be all lowercase")  
        return password1
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError("Password must match")
        return password2
    
 
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        label="Username",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label="Password",
    )