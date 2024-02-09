from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

from models import Payroll, connect_to_database
from forms import SearchForm


load_dotenv()

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]


# @app.route('/')
# def index():
#     form = DistrictForm()
#     form.district.choices = [(d.district) for d in Payroll.query.with_entities(Payroll.district).distinct().all()]

#     page = request.args.get('page', 1, type=int)
#     search_first_name = request.args.get('search_first_name', None)
#     search_last_name = request.args.get('search_last_name', None)
#     search_position = request.args.get('search_position', None)
#     search_district = request.args.get('District', None)
#     per_page = 10

#     payroll_query = Payroll.query

#     if search_first_name:
#         payroll_query = payroll_query.filter(Payroll.first_name.ilike(f'%{search_first_name}%'))
#     if search_last_name:
#         payroll_query = payroll_query.filter(Payroll.last_name.ilike(f'%{search_last_name}%'))
#     if search_position:
#         payroll_query = payroll_query.filter(Payroll.position.ilike(f'%{search_position}%'))
#     if search_district:
#         payroll_query = payroll_query.filter(Payroll.district.ilike(f'%{search_district}%'))

#     pagination = payroll_query.paginate(page=page, per_page=per_page, error_out=False)
#     payroll = pagination.items
#     return render_template("index.html", payroll=payroll, pagination=pagination, search_first_name=search_first_name, search_last_name=search_last_name, search_position=search_position, search_district=search_district, form=form)

@app.route('/')
def index():

    page = request.args.get('page', 1, type=int)
    page_limt = request.args.get('page_limit', 10, type=int)
    per_page = page_limt

    form = SearchForm(request.args, meta={'csrf': False})
    form.district.choices = [('All', 'All')] + [(d.district, d.district) for d in Payroll.query.with_entities(Payroll.district).distinct()]

    payroll_query = Payroll.query
    
    if form.validate():  # If the form is submitted and valid
        search_first_name = form.search_first_name.data
        search_last_name = form.search_last_name.data
        search_position = form.search_position.data
        search_district = form.district.data
    else:
        search_first_name = None
        search_last_name = None
        search_position = None
        search_district = None


    if search_first_name:
        payroll_query = payroll_query.filter(Payroll.first_name.ilike(f'%{search_first_name}%'))
    if search_last_name:
        payroll_query = payroll_query.filter(Payroll.last_name.ilike(f'%{search_last_name}%'))
    if search_position:
        payroll_query = payroll_query.filter(Payroll.position.ilike(f'%{search_position}%'))
    if search_district:
        payroll_query = payroll_query.filter(Payroll.district.ilike(f'%{search_district}%'))

    pagination = payroll_query.paginate(page=page, per_page=per_page, error_out=False)
    payroll = pagination.items

    return render_template("index.html", payroll=payroll, pagination=pagination, search_first_name=search_first_name, search_last_name=search_last_name, search_position=search_position, search_district=search_district, form=form)



if __name__ == "__main__":
    connect_to_database(app)
    app.run(debug=True)