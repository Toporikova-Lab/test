from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
import add
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)

class IntForm(Form):
    message = StringField('Please enter an integer:', validators = [Required()])
    message2 = StringField('Please enter another integer:', validators = [Required()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def starter():
    form = IntForm()
    if form.validate_on_submit():
        session['int1'] = form.message.data
        session['int2'] = form.message2.data
        form.message.data = 0
        form.message2.data = 0
        return redirect(url_for('addition'))
    return render_template('starter.html', form=form)

@app.route('/sum', methods = ['GET', 'POST'])
def addition():
    int1 = int(session.get('int1'))
    int2 = int(session.get('int2'))
    sum = add.summation(int1, int2)
    return render_template("summary.html", sum=sum)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
