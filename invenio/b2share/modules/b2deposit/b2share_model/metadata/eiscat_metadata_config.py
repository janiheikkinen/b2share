from invenio.ext.sqlalchemy import db

domain = 'EISCAT'
# display_name = 'European Incoherent Scatter Scientific Association'
display_name = 'EISCAT'
table_name = 'EISCAT'
image = 'domain-eiscat.png'
kind = 'project'
domaindesc = 'Incoherent scatter radar data'

fields = [
    {
        'name': 'instrument',
        'col_type': db.String(256),
        'display_text': 'Instrument name',
        'description': 'Instrument name',
        'required': True
    },
    {
        'name': 'kindat',
        'col_type': db.String(256),
        'display_text': 'kindat',
        'description': 'kindat',
        'required': True
    },
    {
        'name': 'start_time',
        'col_type': db.String(256),
        'display_text': 'Start time',
        'description': 'Timeserie start time',
        'required': True
    },
    {
        'name': 'end_time',
        'col_type': db.String(256),
        'display_text': 'End time',
        'description': 'Timeserie end time',
        'required': True
    },
    {
        'name': 'kind_of_data_file',
        'col_type': db.String(256),
        'display_text': 'Kind of data file',
        'description': 'Kind of data file',
        'required': True
    },
    {
        'name': 'status',
        'col_type': db.String(256),
        'display_text': 'Status description',
        'description': 'Status description',
        'required': True
    },
    {
        # TODO: Should be joined w/ 'longitude'
        'name': 'latitude',
        'col_type': db.String(256),
        'display_text': 'Instrument latitude',
        'description': 'Instrument latitude',
        'required': True
    },
    {
        # TODO: Should be joined w/ 'latitude'
        'name': 'longitude',
        'col_type': db.String(256),
        'display_text': 'Instrument longitude',
        'description': 'Instrument longitude',
        'required': True
    },
    {
        'name': 'altitude',
        'col_type': db.String(256),
        'display_text': 'Instrument altitude',
        'description': 'Instrument altitude',
        'required': True
    },
]
