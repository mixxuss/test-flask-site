from flask import Flask, abort, render_template, session, url_for, redirect
from data import companies
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# Initialization
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'asdjh12i4uyjasnd123'

class FeedbackForm(Form):
    feedback = StringField('Write your feedback', validators=[Required()])
    submit = SubmitField('Submit')


# View functions
@app.route('/')
def show_index_page():
    return render_template('index.html', companies=companies)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/test/')
def test():
    abort(404)
    # return render_template('testpage.html')


@app.route('/companies/<company>', methods=['GET', 'POST'])
def show_company_page(company):
    form = FeedbackForm()
    if form.validate_on_submit():
        session['name'] = form.feedback.data
        return redirect(url_for('show_company_page', company=company, name=form.feedback.data))
    return render_template('company.html', company=company, form=form, name=session.get('name'))


'''@app.route('/company/<company_name>')
def show_company_page(company_name):
    return "Company %s" % company_name
'''

if __name__ == '__main__':
    app.run(debug=True)
