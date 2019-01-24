from flask import render_template
from application import app
from application.viestit.models import Viesti

@app.route("/")
def index():
    return render_template("index.html", viestit = Viesti.query.all())