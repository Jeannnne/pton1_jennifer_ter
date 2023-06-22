from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm


class CustomLoginForm(AuthenticationForm):
    # Personnalisez votre formulaire de connexion ici si nécessaire
    # Ajoutez des champs supplémentaires ou modifiez le comportement du formulaire selon vos besoins
    pass


class CustomPasswordResetForm(PasswordResetForm):
    # Personnalisez votre formulaire de demande de réinitialisation de mot de passe ici si nécessaire
    # Ajoutez des champs supplémentaires ou modifiez le comportement du formulaire selon vos besoins
    pass


class CustomPasswordChangeForm(SetPasswordForm):
    # Personnalisez votre formulaire de réinitialisation de mot de passe ici si nécessaire
    # Ajoutez des champs supplémentaires ou modifiez le comportement du formulaire selon vos besoins
    pass