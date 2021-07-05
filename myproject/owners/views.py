# myproject/owners/views.py : it contains all the imp routing methods and render_template methods

from flask import Blueprint, render_template, url_for, redirect
from myproject import db  # importing db from __init__.py file, myproject is a dir so init file is getting imported.
from myproject.models import Owner  # importing Owner class
from myproject.owners.forms import AddForm  # importing AddForm method

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprints.route('/add', methods=['GET', 'POST'])  # methods is only required when we have forms
def add():
    print("Inside Add Owner Method")
    form = AddForm()
    if form.validate_on_submit():
        print("Form Add Owner Validated")
        owner_name = form.owner.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(owner_name, puppy_id)
        print("new owner is : ", owner_name)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('puppies.list'))  # Blueprint will link the puppies list method here. We're trying to
    # that to redirect to puppies object and list method.
    return render_template('add_owner.html', form=form)


