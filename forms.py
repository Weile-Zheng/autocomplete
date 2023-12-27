from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class CharacterForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0, max=120)],
                       render_kw={"placeholder": "What is your age?"})
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=100)],
                             render_kw={"placeholder": "What do you do for work? Ex: Late-stage mafia boss"})
    location = StringField('Location', validators=[DataRequired(), Length(max=100)],
                           render_kw={"placeholder": "What region or city are you living in? Ex: Iowa"})
    hobbies = TextAreaField('Hobbies', validators=[DataRequired()],
                            render_kw={"placeholder": "What do you like to do? List some activities. Ex: Origami"})
    personality = TextAreaField('Personality', validators=[DataRequired(), Length(max=200)], render_kw={
        "placeholder": "How would you describe yourself? For example, list three adjectives or what you think would be on your tombstone."})


class EventForm(FlaskForm):
    event = TextAreaField('Event', validators=[DataRequired(), Length(max=100)], render_kw={
        "placeholder": "What is the event that should happen? Ex: Unchecked climate change, winning the lottery, losing a lottery ticket, etc."})
