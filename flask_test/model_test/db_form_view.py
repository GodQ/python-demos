from . import bp
from .models import Test
from flask import render_template
from flask import request


@bp.route("/db_form", methods=['GET', 'POST'])
def db_form():
    submit_type = request.form.get("type")
    if submit_type:
        if submit_type == 'insert' and 'insert-name' in request.form and request.form.get('insert-name'):
            insert_name = request.form.get('insert-name')
            test = Test(insert_name)
            test.save()
        elif submit_type == 'delete' and 'delete-name' in request.form and request.form.get('delete-name'):
            delete_name = request.form.get('delete-name')
            Test.delete_by_name(delete_name)
        elif submit_type == 'delete_all':
            Test.delete_all()

    all = Test.query.all()
    context = {
        "data_list": all
    }
    return render_template("db_form.html", **context)

