from django import forms
from django.core.mail import EmailMessage
from .models import *

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['nombre']
        mail = self.cleaned_data['email']
        message = self.cleaned_data['mensaje']
        email = "Correo enviado por: %s \nSu correo electronico es: %s \nSu mensaje es: %s ." %(name, mail,message)
        correo = EmailMessage('Web Doctorado en Derecho-Uach Contacto', email,'infoder@uach.cl',to=['eevp88@gmail.com'])
        correo.send()
        pass

class PostulacionForm(forms.Form):
    """docstring for PostulacionForm"""
    class Meta:
        model = Postulacion
