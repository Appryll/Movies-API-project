# Movies API project

## API REST pour gérer les films.

## Résumé
## Index
1. [Mise en place du projet](#local)
    - [Windows](#windows)
    - [MacOS, Linux](#macl)
2. [Remplir la bdd](bdd)
3. [Documentation de l'API](#swagger)
4. [Test Unitaires](#test)

### Mise en place du projet<a name="local"></a>

#### I) Windows : <a name="windows"></a
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet :

    $ git clone https://github.com/Appryll/Movies-API-project.git

    Se déplacer dans le repertoire du projet :

    $ cd Movies-API-project-master

###### -Créer et activer l'environnement virtuel :
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis :
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    $ python manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python manage.py runserver <your_port>

###### - Naviguer sur le site :
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel :
    deactivate

-----
#### II) MacOS, Linux : <a name="macl"></a
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet :
     $ git clone https://github.com/Appryll/Movies-API-project.git

    Se déplacer dans le repertoire du projet :
    $ cd Movies-API-project-master

###### -Créer et activer l'environnement virtuel :
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis :
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    $ python3 manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas 
    disponible :
    $ python3 manage.py runserver <your_port>

###### - Naviguer sur le site :
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel :
    deactivate

------------------------------------------------------------------------------------------------------------------------
### Remplir la bdd <a name="bdd"></a>
    $ python intodb.py
### Documentation de l'API <a name="swagger"></a>
    Disponible à l'adresse : http://127.0.0.1:8000/docs/

#### Test Unitaires <a name="test"></a>
    $ python manage.py test