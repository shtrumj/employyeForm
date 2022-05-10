from flask import Blueprint, render_template,request, url_for, flash,redirect
views_blueprint = Blueprint("views", __name__, static_folder="static", template_folder="templates")

Employees = []


@views_blueprint.route('/')
def form():
    if request.method == 'POST':
        first_name = request.form['EmployeeFirstName']
        last_name = request.form['EmployeeLastName']
        Employees.append({'first_name': first_name, 'last_name':last_name})
    return render_template('form.html',methods=('GET','POST'))
