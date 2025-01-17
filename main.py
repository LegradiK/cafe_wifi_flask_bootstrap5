from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, BooleanField
from wtforms.validators import DataRequired, URL
import pandas as pd
import os

app = Flask(__name__)

# don't forget to source data.env file before running
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
Bootstrap5(app)


class HikingForm(FlaskForm):
    name = StringField('Name ', validators=[DataRequired()])
    ratings = SelectField('Ratings', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    difficulty = SelectField('Difficulty', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    google_map = StringField('Google map link', validators=[DataRequired(),URL(require_tld=True, message='googlemap location link required')])
    hike_distance = FloatField('Hike Distance (in km)', validators=[DataRequired()])
    home_distance = FloatField('Distance from Home (in km) ', validators=[DataRequired()])
    parking = BooleanField('Parking Available ')
    toilet = BooleanField('Toilets available ')

CVS_FORM = './hiking-data.cvs'

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add():
    form = HikingForm()
    if form.validate_on_submit():
        print("True")
        
    return render_template('add.html', form=form)


@app.route('/hikes')
def hikes():
    datafile = pd.read_csv('hiking-data.csv')
    data = datafile.to_dict(orient='records')
    return render_template('hiking_places.html', hills=data)


if __name__ == '__main__':
    app.run(debug=True)
