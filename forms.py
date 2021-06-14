from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


class WalletForm(Form):
	wallet = TextField('Wallet Address', validators=[validators.DataRequired()])
