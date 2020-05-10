from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    address = Col("Address")
    birthday = Col('Birthday')
    email = Col('Email')
    profession = Col('Profession')
    interests = Col('Interests')
    phone_number = Col('Phone number')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
