from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Payroll(db.Model):

    __extends_existing__ = True

    __tablename__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), nullable=False)
    usd = db.Column(db.String, nullable=False)
    district = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    total_pay = db.Column(db.Text, nullable=False)



# @app.route('/')
# def index():
#     page = request.args.get('page', 1, type=int)
#     search_query = request.args.get('search', '')
#     sort_field = request.args.get('sort', 'id')  # Default sort field
#     sort_direction = request.args.get('direction', 'asc')  # Default sort direction
#     per_page = 10

#     payroll_query = Payroll.query
    
#     if search_query:
#         payroll_query = payroll_query.filter(
#             db.or_(
#                 Payroll.first_name.ilike(f'%{search_query}%'),
#                 Payroll.last_name.ilike(f'%{search_query}%'),
#                 Payroll.position.ilike(f'%{search_query}%')
#             )
#         )
    
#     if sort_direction == 'desc':
#         payroll_query = payroll_query.order_by(db.desc(getattr(Payroll, sort_field)))
#     else:
#         payroll_query = payroll_query.order_by(getattr(Payroll, sort_field))
    
#     pagination = payroll_query.paginate(page=page, per_page=per_page, error_out=False)
#     payroll = pagination.items
#     return render_template("index.html", payroll=payroll, pagination=pagination, search_query=search_query, sort_field=sort_field, sort_direction=sort_direction)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    search_first_name = request.args.get('search_first_name', '')
    search_last_name = request.args.get('search_last_name', '')
    search_position = request.args.get('search_position', '')
    sort_field = request.args.get('sort', 'id')
    sort_direction = request.args.get('direction', 'asc')
    per_page = 10

    payroll_query = Payroll.query

    if search_first_name:
        payroll_query = payroll_query.filter(Payroll.first_name.ilike(f'%{search_first_name}%'))
    if search_last_name:
        payroll_query = payroll_query.filter(Payroll.last_name.ilike(f'%{search_last_name}%'))
    if search_position:
        payroll_query = payroll_query.filter(Payroll.position.ilike(f'%{search_position}%'))

    if sort_direction == 'desc':
        payroll_query = payroll_query.order_by(db.desc(getattr(Payroll, sort_field)))
    else:
        payroll_query = payroll_query.order_by(getattr(Payroll, sort_field))

    pagination = payroll_query.paginate(page=page, per_page=per_page, error_out=False)
    payroll = pagination.items
    return render_template("index.html", payroll=payroll, pagination=pagination, search_first_name=search_first_name, search_last_name=search_last_name, search_position=search_position, sort_field=sort_field, sort_direction=sort_direction)



if __name__ == "__main__":
    app.run(debug=True)