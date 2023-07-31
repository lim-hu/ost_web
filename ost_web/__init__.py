from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from .skill_file import oblivion_attributes, oblivion_skills

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:root@localhost/ost'
db = SQLAlchemy(app)

class Skills(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer(), nullable=False, unique=True, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    attribute = db.Column(db.String(), nullable=False)
    count = db.Column(db.Integer(), nullable=False, default=0)
    

class Attributes(db.Model):
    __tablename__ = "attributes"
    id = db.Column(db.Integer(), nullable=False, unique=True, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    count = db.Column(db.Integer(), nullable=False, default=0)
    
    
@app.route("/", methods=["POST", "GET"])
def skill_list():
    skills = Skills.query.order_by(Skills.id).all()
    attributes = Attributes.query.order_by(Attributes.id).all()
    
    o_attrs = {
    "STR": 0,
    "END": 0,
    "SPD": 0,
    "AGI": 0,
    "PER": 0,
    "INT": 0,
    "WIL": 0
}
    
    for attr in attributes:
        skill_attrs = Skills.query.filter_by(attribute=attr.name).all()
        for skill_attr in skill_attrs:
            o_attrs[skill_attr.attribute] +=skill_attr.count
        
    for o_attr in o_attrs:
        edit_counter = Attributes.query.filter_by(name=o_attr).first()
        if o_attrs[o_attr] == 10:
            edit_counter.count = 5    
        elif o_attrs[o_attr] >=8 and o_attrs[o_attr] < 10:
            edit_counter.count = 4 
        elif o_attrs[o_attr] >=5 and o_attrs[o_attr] < 8:
            edit_counter.count = 3 
        elif o_attrs[o_attr] >=1 and o_attrs[o_attr] < 5:
            edit_counter.count = 2 
        elif o_attrs[o_attr] < 1:
            edit_counter.count = 1
            
    db.session.commit()

    return render_template("home.html", skills=skills, attributes=attributes)

@app.route("/create_all")
def create_all():
    db.create_all()
    for skill in oblivion_skills:
        q_skill = Skills.query.filter_by(name=skill).first()
        if not q_skill:
            s = Skills(name=skill, attribute=oblivion_skills[skill])
            db.session.add(s)

    for attribute in oblivion_attributes:
         q_attributes = Attributes.query.filter_by(name=attribute).first()
         if not q_attributes:
             a = Attributes(name=attribute)
             db.session.add(a)
             
    db.session.commit()
    return "Database filled"


@app.route("/add", methods=["POST"])
def add_counter():
    key_dict = request.form.to_dict()
    skill_update = key_dict["add"]
    query_skill = Skills.query.filter_by(name=skill_update).first()
    if query_skill:
        query_skill.count += 1
        if query_skill.count >= 10:
            query_skill.count = 10
        db.session.commit()
        return redirect("/")
    
    return redirect("/")

@app.route("/sub", methods=["POST"])
def sub_counter():
    key_dict = request.form.to_dict()
    skill_update = key_dict["sub"]
    query_skill = Skills.query.filter_by(name=skill_update).first()
    if query_skill:
        query_skill.count -= 1
        if query_skill.count <= 0:
            query_skill.count = 0
        db.session.commit()
        return redirect("/")
    
    return redirect("/")

@app.route("/levelup", methods=["POST"])
def levelup():
    query_skills = Skills.query.all()
    query_attrs = Attributes.query.all()
    for query_skill in query_skills:
        query_skill.count = 0
        
    for query_attr in query_attrs:
        query_attr.count = 0
        
    db.session.commit()
    return redirect("/")


