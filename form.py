from flask_wtf import Form
from wtforms import validators, StringField, IntegerField, SelectField, PasswordField, TextAreaField, BooleanField

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

	password = PasswordField('Password',
		[validators.DataRequired(message="Password required")]
		)

	size = SelectField('Size', choices=[('7','7'), ('10','10'), ('12','12'), ('99', 'CS'), ('100', 'CD')])

	mail = BooleanField()


class LoginForm(Form):
	username = StringField('Username',
		[validators.DataRequired(message="Username is required")]
		)

	password = PasswordField('Password',
		[validators.DataRequired(message="Password required")]
		)


class AddPost(Form):
	title = StringField('Title',
		[validators.DataRequired(message="Title is required")]
		)

	timestamp = StringField('Timestamp',
		[validators.DataRequired(message="Timestamp is required")]
		)

	ghlink = StringField('Github Link')

	content = TextAreaField('Body',
		[validators.DataRequired(message="Body is required")]
		) 