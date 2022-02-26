from flask import Flask, render_template, request
from forms import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd

DEBUG = True
app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/", methods=['GET', 'POST'])
def index():
    form = WalletForm(request.form)
    if(request.method == 'POST'):		#If the user submits data in the Form
        if(form.validate()):		#If form is validated
            data = pd.read_csv("c_airdrop.csv")
            wallet_address = request.form['wallet'].lower()
            print(wallet_address.lower())
            addresses = data['Address'].values.tolist()
            end_votes = data['End votes'].values.tolist()
            payout = data['CRE8R Payout'].values.tolist()
            if(wallet_address in addresses):
                return render_template("airdrop-confirmation.html", end_votes = end_votes[addresses.index(wallet_address)], payout = payout[addresses.index(wallet_address)])
            else:
                return render_template("sorry.html")

    return render_template("index.html", form=form)

if(__name__ == "__main__"):
	app.run(host="localhost", port=8888)
