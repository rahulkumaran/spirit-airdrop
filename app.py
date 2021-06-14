from flask import Flask, render_template, request
from forms import *
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


DEBUG = True
app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/", methods=['GET', 'POST'])
def index():
    form = WalletForm(request.form)
    if(request.method == 'POST'):		#If the user submits data in the Form
        if(form.validate()):		#If form is validated
            wallet_address = request.form['wallet']
            print(wallet_address.lower())
            addresses = open('address.txt','r')
            for line in addresses:
                line = line.replace('\n','')
                if(wallet_address.lower()==line):
                    print(wallet_address.split(), line.split())
                    return render_template("airdrop-confirmation.html")
            return render_template("sorry.html")

    return render_template("index.html", form=form)

if(__name__ == "__main__"):
	app.run(host="localhost", port=5000)
