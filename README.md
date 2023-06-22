# pton1_jennifer_ter

Utilier un .env pour les variables d'environnements

Pour l'authentification j'utilise les classes préfaite de django.contrib.auth tel que LoginView ... et la convention 
Par conséquent, je ne rajoute pas plusieurs choses tel que le template name car j'ai suivi la convention, 

    # Old version
    class CustomPasswordResetView(PasswordResetView):
        success_url = 'password_reset_done'
        email_template_name = 'registration/password_reset_email.html'
        form_class = CustomPasswordResetForm

    # New version
    class CustomPasswordResetView(PasswordResetView):
        form_class = CustomPasswordResetForm
    

