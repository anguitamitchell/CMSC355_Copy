from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, widgets, IntegerField, FieldList, FormField, DecimalField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, NumberRange
from backend.tables import User

# Sets up the form on the register page
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    first_name = StringField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "First Name"})
    last_name = StringField(validators=[InputRequired(), Length(min=1)], render_kw={"placeholder": "Last Name"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user = User.query.filter_by(
            username=username.data).first()
        if existing_user:
            raise ValidationError(
                "That username already exists."
            )
        

# Sets up form on login page
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")


class SurveyForm(FlaskForm):
    fitness_goals = SelectMultipleField(
        "What are your fitness goals?",
        choices=[
            ("Build Muscle", "Build Muscle"),
            ("Lose Weight", "Lose Weight"),
            ("Increase Strength", "Increase Strength"),
            ("Improve Cardio", "Improve Cardio")
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )

    submit = SubmitField("Submit")


class FitnessLogWorkoutForm(FlaskForm):
    legs_reps = IntegerField('Total Reps', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])
    legs_sets = IntegerField('Total Sets', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    chest_reps = IntegerField('Total Reps', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])
    chest_sets = IntegerField('Total Sets', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    back_reps = IntegerField('Total Reps', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])
    back_sets = IntegerField('Total Sets', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    bicep_reps = IntegerField('Total Reps', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])
    bicep_sets = IntegerField('Total Sets', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    tricep_reps = IntegerField('Total Reps', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])
    tricep_sets = IntegerField('Total Sets', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    submit = SubmitField("Submit")

class FitnessLogCardioForm(FlaskForm):
    miles = DecimalField('Total Miles', default=0, validators=[NumberRange(min=0, message="Value must be 0 or greater")])

    submit = SubmitField("Submit")