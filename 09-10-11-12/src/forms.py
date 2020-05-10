# forms.py

from wtforms import Form, StringField, SelectField, validators


class ContactsSearchForm(Form):
    choices = [('Name', 'Name'),
               ('Birthday', 'Birthday'),
               ('Email', 'Email'),
               ('Profession', "Profession"),
               ('Interests', 'Interests'),
               ('Phone number', 'Phone number')]

    select = SelectField('Search for contacts by criteria:', choices=choices)
    search = StringField('')


class ContactForm(Form):
    name = StringField('Name')
    address = StringField('Address')
    birthday = StringField('Birthday')
    email = StringField('Email')
    profession = StringField('Profession')
    interests = StringField('Interests')
    phone_number = StringField('Phone number')
