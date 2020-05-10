# main.py
import time
from app import app
from db_setup import init_db, db_session
from forms import ContactsSearchForm, ContactForm
from flask import flash, render_template, request, redirect, url_for
from models import Contact, User
from tables import Results
from app import db
from flask_bootstrap import Bootstrap
from login_forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
init_db()
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(int(user_id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db_session.query(User).filter_by(
            username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect("/")

        flash('Incorrect login details. Keep in mind that both password and username are case sensitive')
        return redirect("/login")
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        try:
            new_user = User(username=form.username.data,
                            email=form.email.data, password=hashed_password)
            db_session.add(new_user)
            db_session.commit()
            flash("Successful registration")
            return redirect("/login")
        except:
            flash("email or username is already taken")
            return redirect("/login")
        # return '<h1>New user has been created!</h1>'
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    search = ContactsSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
@login_required
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:

        if search.data['select'] == 'Name':
            qry = db_session.query(Contact).filter(
                Contact.name.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Address':
            qry = db_session.query(Contact).filter(
                Contact.address.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Birth day':
            qry = db_session.query(Contact).filter(
                Contact.birthday.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Phone number':
            qry = db_session.query(Contact).filter(
                Contact.phone_number.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Email':
            qry = db_session.query(Contact).filter(
                Contact.email.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Profession':
            qry = db_session.query(Contact).filter(
                Contact.profession.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Interests':
            qry = db_session.query(Contact).filter(
                Contact.interests.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Contact)
            results = qry.all()
    else:
        qry = db_session.query(Contact)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_contact', methods=['GET', 'POST'])
@login_required
def new_contact():
    """
    Add a new contact
    """
    form = ContactForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the contact
        contact = Contact()
        save_changes(contact, form, new=True)
        flash('Contact created successfully!')
        return redirect("/")

    return render_template('new_contact.html', form=form)


def save_changes(contact, form, new=False):
    """
    Save the changes to the database
    """

    contact.name = form.name.data
    contact.address = form.address.data
    contact.birthday = form.birthday.data
    contact.email = form.email.data
    contact.profession = form.profession.data
    contact.interests = form.interests.data
    contact.phone_number = form.phone_number.data

    if new:
        # Add the new contact to the database
        db_session.add(contact)

    # commit the data to the database
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """
    Add / edit an item in the database
    """
    qry = db_session.query(Contact).filter(
        Contact.id == id)
    contact = qry.first()

    if contact:
        form = ContactForm(formdata=request.form, obj=contact)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(contact, form)
            flash('Contact updated successfully!')
            return redirect('/')
        return render_template('edit_contact.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db_session.query(Contact).filter(
        Contact.id == id)
    contact = qry.first()

    if contact:
        form = ContactForm(formdata=request.form, obj=contact)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db_session.delete(contact)
            db_session.commit()

            flash('Contact deleted successfully!')
            return redirect('/')
        return render_template('delete_contact.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)
