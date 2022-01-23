from flask import Blueprint, redirect, render_template, request,url_for, session
from .forms import CarInfoForm
from car_inventory.models import Car, db

from car_inventory.site.forms import CarInfoForm
"""
Note that in the above code, 
some arguments are specified when creating the Blueprint object. 
The first argument, "site", is the Blueprint’s name, 
which is used by Flask’s routing mechanism. 
The second argument, __name__, is the Blueprint’s import name, 
which Flask uses to locate the Blueprint’s resources.
"""

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')
    

@site.route('/profile', methods = ['GET', 'POST'])
def profile():
    form = CarInfoForm()
    if request.method == 'POST' and form.validate():
        year = form.year.data
        make = form.make.data
        model = form.model.data
        color = form.color.data
        image = form.image.data
        created_by = session['id']

        car = Car(year,make,model,color,image,created_by)
        db.session.add(car)
        db.session.commit()

        return render_template('profile.html', 
            form = form,
            year = year,
            make = make,
            model = model,
            color = color,
            image = image)

    return render_template('profile.html', form = form)



    

    

