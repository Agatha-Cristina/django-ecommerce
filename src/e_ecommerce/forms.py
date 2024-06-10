from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        error_messages={'invalid': 'É obrigatorio o preenchimento do nome!'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
            )
    email = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido'},
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            "placeholder": "Digite seu email"
            }
        )
    )
    content = forms.CharField(
        error_messages={'invalid': 'É obrigatorio o preenchimento do campo mensagem!'},
            widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
    )
    def clean_mail(self):
        email= self.cleaned_data.get("Email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O email deve ser do gmail.com")
        return email