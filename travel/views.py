from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":

        query = "%" + request.args['search'] + "%"

        # Selecting the name of the Destination:
        # destinations = db.session.scalars(db.select(Destination).where(Destination.name.like(query)))
        
        # Selecting the description of the Destination:
        # destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))

        # Use db.or_ for the OR condition for selecting both name and desciption of the Destination:
        destinations = db.session.scalars(
            db.select(Destination).where(
                db.or_(
                    Destination.name.like(query),
                    Destination.description.like(query)
                )
            )
        )

        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))