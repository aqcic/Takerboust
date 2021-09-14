# Sur le Projet
collecte, traitement et affichage des données des habitants Takerboustois (profession et étude)

# Configuration de l'environnement de travail :
- Tout d'abord il faut télécharger le projet sur votre PC en utilisant GIT: 
```
git clone https://github.com/aqcic/Takerboust.git
```
Puis: 

```
cd Takerboust
```
- Installations requises: 

```
pip install -r requirements.txt
```

- Création de la base de donnée: 
  dans le meme dossier " Takerboust" vous devez ouvrir l'invite de commande puis lancer python: 

```
	python
```
```
	From app import db
```
```
	db.create_all()
```
- voila, maintenant il ne vous reste que de démarez le projet en clickant sur "app.py" ou: 
```
	python app.py
```
ou 

```
<<<<<<< HEAD
	flask run
```
=======
flask run
```

Merci ...
>>>>>>> fd2d45e80fb86ef647e171f733384c56051fd0b0
