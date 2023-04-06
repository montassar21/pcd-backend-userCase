from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Predict(db.Model):
    __tablename__='Predict'
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    Gender=db.Column(db.Integer)
    marital_status=db.Column(db.Integer)
    age=db.Column(db.Integer)
    scolarship=db.Column(db.Integer)
    mother_qualification=db.Column(db.Integer)
    mother_occupation=db.Column(db.Integer)
    father_occupation=db.Column(db.Integer)
    inflation_rate=db.Column(db.Integer)
    previous_qualifcation=db.Column(db.Integer)
    course=db.Column(db.Integer)
    curricular_units_1st_sem_without_evaluations=db.Column(db.Integer)
    curricular_units_1st_sem_approved=db.Column(db.Integer)
    curricular_units_1st_sem_credited=db.Column(db.Integer)
    curricular_units_1st_sem_with_evaluations=db.Column(db.Integer)
    curricular_units_2nd_sem_without_evaluations=db.Column(db.Integer)
    curricular_units_2nd_sem_approved=db.Column(db.Integer)
    curricular_units_2nd_sem_credited=db.Column(db.Integer)
    curricular_units_2nd_sem_with_evaluations=db.Column(db.Integer)

    def __init__(self,Gender,marital_status,age,scolarship,mother_qualification,mother_occupation,father_occupation,inflation_rate,previous_qualifcation
    ,course,curricular_units_1st_sem_approved,curricular_units_1st_sem_credited,curricular_units_1st_sem_with_evaluations,curricular_units_1st_sem_without_evaluations,curricular_units_2nd_sem_approved,curricular_units_2nd_sem_credited,curricular_units_2nd_sem_with_evaluations,curricular_units_2nd_sem_without_evaluations):
        self.Gender=Gender
        self.marital_status=marital_status
        self.age=age
        self.scolarship=scolarship
        self.mother_occupation=mother_occupation
        self.mother_qualification=mother_qualification
        self.father_occupation=father_occupation
        self.inflation_rate=inflation_rate
        self.previous_qualifcation=previous_qualifcation
        self.course=course
        self.curricular_units_1st_sem_approved=curricular_units_1st_sem_approved
        self.curricular_units_1st_sem_credited=curricular_units_1st_sem_credited
        self.curricular_units_1st_sem_with_evaluations=curricular_units_1st_sem_with_evaluations
        self.curricular_units_1st_sem_without_evaluations=curricular_units_1st_sem_without_evaluations
        self.curricular_units_2nd_sem_approved=curricular_units_2nd_sem_approved
        self.curricular_units_2nd_sem_credited=curricular_units_2nd_sem_credited
        self.curricular_units_2nd_sem_with_evaluations=curricular_units_2nd_sem_with_evaluations
        self.curricular_units_2nd_sem_without_evaluations=curricular_units_2nd_sem_without_evaluations
    def json(self):
        return {"Gender":self.Gender,"marital_status":self.marital_status,"age":self.age,"scolarship":self.scolarship,"mother_qualification":self.mother_qualification,"mother_occupation":self.mother_occupation,
       "father_occupation":self.father_occupation,"inflation_rate":self.inflation_rate,"previous_qualifcation":self.previous_qualifcation,"course":self.previous_qualifcation,"curricular_units_1st_sem_approved":self.curricular_units_1st_sem_approved,"curricular_units_1st_sem_credited":self.curricular_units_1st_sem_credited,
       "curricular_units_1st_sem_with_evaluations":self.curricular_units_1st_sem_with_evaluations,"curricular_units_1st_sem_without_evaluations":self.curricular_units_1st_sem_without_evaluations,"curricular_units_2nd_sem_approved":self.curricular_units_2nd_sem_approved,"curricular_units_2nd_sem_credited":self.curricular_units_2nd_sem_credited,
       "curricular_units_2nd_sem_with_evaluations":self.curricular_units_2nd_sem_with_evaluations,"curricular_units_2nd_sem_without_evaluations":self.curricular_units_2nd_sem_without_evaluations }