# pton1_jennifer_ter

# Configuration
Pour les variables d'environnements, j'ai utilisé un fichier .env


# Authentification
Pour les vues, j'utilise les classes préfaites de django.contrib.auth, telles que LoginView, PasswordResetConfirmView....
De plus, puisque je suis la convention, je n'ajoute pas plusieurs éléments comme le nom du template dans mes classes vues.

Par contre pour les vues dans "users", j'ai garder l'option template_name car je voulais ne pas oublier que les templates étaient lier a cette vue.

# Ancienne version
class CustomPasswordResetView(PasswordResetView):
    success_url = 'password_reset_done'
    email_template_name = 'registration/password_reset_email.html'
    form_class = CustomPasswordResetForm

# Nouvelle version
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm

J'ai ajouté la classe LoginRequiredMixin à CustomPasswordChangeView et CustomPasswordChangeDoneView, ainsi seuls les utilisateurs connectés peuvent changer leur mot de passe.


# Options supplémentaires
Il y a l'option "Mot de passe oublié" lors de la connexion sur la page "users/login".
Afin de changer son mot de passe, un email est envoyé à l'utilisateur avec un lien pour le changer. 

L'email est envoyé dans la console avec un lien fonctionnel pour changer son mot de passe.


# Le model User
Pour les utilisateurs, j'ai recréé mon modèle User appelé Collaborator, qui hérite d'AbstractUser car AbstractUser contient déjà (username, first name, lastname, email). 
En créant une classe qui hérite d'AbstractUser, je peux ajouter des champs tels que le poste et la direction actuelle pour correspondre au sujet, tout en bénéficiant des champs déjà présents dans AbstractUser.

# Validation des champs du User
Pour la validation des champs email et numéro de téléphone , j'ai utilisé des classes spéciales qui effectuent automatiquement la validation du format. 
De plus, pour le numéro de téléphone, j'ai précisé le format attendu dans les paramètres de la définition du champ.

    phone_number = PhoneNumberField(
                 blank=True, 
                 region='FR',
                 help_text="Entrez un numéro de téléphone au format français (par exemple, 0612345678)."
    )

# Options supplémentaires
Pour la date d'arrivée, j'ai utilisé un widget de type date picker pour faciliter la saisie de la date.

# Axes d'amélioration
J'aurais pu utiliser from django.utils.translation import gettext_lazy as _ pour faciliter la traduction de mon application en plusieurs langages, mais je n'ai pas eu le temps.


# Précisions sur les services et les images
Pour les services, j'ai créé un object qui contient un parent (un objet du même type) et un nom afin de hiérarchiser les services présentés, comme indiqué dans le sujet.

Aussi, j'ai réécrit la méthode __str__ afin d'afficher l'arborescence complète du service (par exemple, "DEV" devient "DSI/DEV")


Pour les images, j'ai ajouté une variable dans settings.py afin de pouvoir changer la source de l'image si nécessaire.
De plus, pour chaque nouvel utilisateur, une nouvelle image est téléchargée, ce qui permet de savoir si un nouvel utilisateur a été créé au lieu d'utiliser toujours la même image par défaut.
   S'il fallait que chaque nouvel utilisateur ait la même image par défaut, le code s'adapterai bien puisqu'il suffirait de changer une seule fonction qui se trouve dans la classe User : 

    def save(self, *args, **kwargs):
         if not self.profile_picture:
            response = requests.get(settings.DEFAULT_IMAGE_LINK, stream=True)
            response.raise_for_status()

            if response.ok:
                image_file = BytesIO(response.content)
                self.profile_picture.save(settings.DEFAULT_IMAGE_NAME, File(image_file))

            else:
                print("Error while downloading default image")

        super().save(*args, **kwargs)

Après avoir vérifier si l'utilisateur a renseigné une image. Il faudra rajouter un check sur l'existance d'une image par défaut puis on la sélectionnerait au lieu d'en télécharger une nouvelle.


De plus avec cette configuration, le répertoire default_images sera créé automatiquement lorsque le module config sera importé dans settings.py.
