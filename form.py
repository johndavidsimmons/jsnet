from flask_wtf import Form
from wtforms import validators, StringField, IntegerField, SelectField

class AddRecord(Form):
	artist = StringField('Artist',
		[validators.DataRequired(message="Artist is required")]
		)

	title = StringField('Title',
		[validators.DataRequired(message="Title is required")]
		)

	color = StringField('Color',
		[validators.DataRequired(message="Color is required")]
		)

	year = IntegerField('Year',
		[validators.DataRequired(message="Year is required")]
		)

	notes = StringField('Notes')

	password = StringField('Password',
		[validators.DataRequired(message="Password required")]
		)

	size = SelectField('Size', choices=[('7','7'), ('10','10'), ('12','12'), ('99', 'CS'), ('100', 'CD')])
