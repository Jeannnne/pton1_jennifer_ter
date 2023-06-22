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

J'ai rajouter la class LoginRequiredMixin sur CustomPasswordChangeView et CustomPasswordChangeDoneView,
comme ca uniquement les utilisateurs connectés peuvent changer leur mot de passe.

Pour les user j'ai re-créer mon User qui s'appelle Collaborator, il herite d'AbstractUser car AbstractUser contient deja (username, first name, lastname, email, date_joined)
En creant une classe heritant d'AbstractUser, je peux rajouter des champs tel que le poste, la direction actuelle pour correspondre au sujet tout en beneficiant des champs deja present d'AbstractUser

Pour les validations des champs email, numero de telephone, et date d'arrivee, j'ai utiliser des classes spéciales qui font automatiquement la validation du format.
De plus pour le numerio de telephone, j'ai renseigné le format attendu dans les parametres de la définition du champ .

    phone_number = PhoneNumberField(
                     blank=True, 
                     region='FR',
                     help_text="Entrez un numéro de téléphone au format français (par exemple, 0612345678)."
    )

Pour la date d'arrivée, j'ai utilisé un widget de type date picker pour faciliter la saisie de la date.

J'aurais pu utuliser from django.utils.translation import gettext_lazy as _
 pour faciliter la traduciton de mon app en plusieurs langages mais je n'ai pas eu le temps.


