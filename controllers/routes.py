from flask import render_template
from ..app import app
from .expense_data import *


#@app.route('/', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET'])
def home():
    values = {
        "income" : income_data, 
        "expense": expense_data, 
        "income_summary":income_summary_data, 
        "expense_summary":expense_summary_data, 
        "dow": days_of_week
    }
    return render_template("index.html", data=values)
#end def

