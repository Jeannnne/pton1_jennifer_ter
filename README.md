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

Il y a possiilité de clicker sur le boutton mot de passe oublier, avec un formulaire pour envoyer son email afin de changer le mot de passe.
Pour l'instant l'email est envoyé sur le terminal, mais il est possible de le configurer pour qu'il soit envoyé sur une adresse mail.
Un lien est genéré avec un token pour changer le mot de passe.

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



Pour les services, j'ai créer une table qui contient un parent (un object du meme type) et un nom afin de hierachiser les services présenter comme dans le sujet.

Pour les images j'ai rajouter une variable dans settings.py comme ca si on veut changer la source de l'image on peut 
De plus pour chaque nouveau user, on telecharge une nouvelle image, ca permet de savoir si un novueau user à été créer au lieu d'utiliser toujours la meme image par defaut.
(Ou est ce qu'il faut telecharger une fois puis reutilsier l'image ? )

Avec cette configuration, le répertoire default_images sera créé automatiquement lorsque le module config sera importé dans settings.py.

Pour les servces j'ai réecris la fonction str afin de visualiser l'arborescence compltete du service (ex= DEV devient DSI/DEV).

Pour le stockage des images c'est vrai que ca serait mieux de faire un renommage automatique avec prends le nom de l'app en question et qui créer des sous dossiers pour qu'on ait :

    media/APP_NAME/images/IMAGE_NAME

C'est plus propre et plus facile à retrouver. Mais je ne l'ai pas fait pour l'instant par manque de temps.

Pour le home de l'annuaire j'ai fait en sorte que si on click sur l'image, on peut aussi acceder a la page du user
Dans l hom de l'annuaire j'ai trié la liste des services pour avoir le plus global en premier et les plus specifique en bas.

Pour la modification d'un profile j'ai fait deux sécurité, avec le path on ne peux pas accéder au formulaire pour la modification si ce n'est pas notre page
De plus sur la page d'un detail, le boutton update n'est visible que lorsque l'utilisateur est sur sa propre page.
