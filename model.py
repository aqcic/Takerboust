from app import db

class Student(db.model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)
    niveau_etude = db.Column(db.String(10), nullabale=False)
    annee_etude = db.Column(db.Integer, nullable=False)
    universite = db.Column(db.String(100), nullable=False)
    specialite = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return "Student %r" % self.id
        
