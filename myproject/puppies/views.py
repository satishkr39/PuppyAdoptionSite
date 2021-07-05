# inside myproject/puppies/views.py

from flask import render_template, url_for, Blueprint, redirect
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

# Home Page for Add Puppy
@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    print(form.name.data)
    print("insdie Add pup method ")
    if form.validate_on_submit():
        print("Inside Add pup Validate ")
        name = form.name.data  # get the data from field
        new_pup = Puppy(name)  # we need to add the name to our model class so creating object.
        db.session.add(new_pup)  # adding to our model table
        print("Puppy Added : ", new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))  # if all validated then reidrect to list page
    return render_template('add.html', form=form)  # to render the add page

@puppies_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    print(puppies)
    return render_template('list.html', puppies=puppies)

@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data  # get the data from INT filed
        pupp = Puppy.query.get(id)  # we will get only 1 puppy
        db.session.delete(pupp)
        db.session.commit()
        print("Puppy Deleted: ",pupp)
        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)

