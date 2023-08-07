from flask import Flask, render_template, request, redirect
from .skill_file import o_attributes, o_skills

app = Flask(__name__)
    
@app.route("/", methods=["POST", "GET"])
def skill_list():
    return render_template("skills.html", o_skills=o_skills, o_attributes=o_attributes)

# y

