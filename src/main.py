from app import create_app
from app.firestore_service import add_todo
from app.firestore_service import delete_todo
from app.firestore_service import get_todos
from app.firestore_service import update_todo
from app.firestore_service import update_todo_status_db
from app.forms import DeleteAccountForm
from app.forms import TodoForm
from app.forms import UpdateTodoForm
from flask_login import current_user
from flask_login import login_required
from flask import flash
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for


app = create_app()


@app.route('/')
def home_no_auth():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('home-no-auth.html')


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user_id = current_user.id
    update_todo_form = UpdateTodoForm()
    todo_form = TodoForm()
    delete_account_form = DeleteAccountForm()
    
    context = {
        "user_id": user_id,
        "todo_form": todo_form,
        "delete_todo": delete_todo,
        "update_todo": update_todo,
        "todos": get_todos(user_id),
        "update_todo_form": update_todo_form,
        "delete_account_form": delete_account_form,
    }

    #Adding todo
    if todo_form.validate_on_submit():
        description = todo_form.description.data
        add_todo(
            user_id = user_id, 
            description = description
        )
        return redirect(url_for('home'))
    elif request.method == 'POST':
        flash('Type something first')
    return render_template('home.html', **context)


@app.route('/todos/delete/<todo_id>')
@login_required
def delete_todos(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)
    return redirect(url_for('home'))


@app.route('/todos/update/<todo_id>', methods=['POST'])
@login_required
def update_todos(todo_id):
    update_todo_form = UpdateTodoForm()

    if update_todo_form.validate_on_submit():
        new_todo = update_todo_form.description.data
        user_id = current_user.id
        update_todo(user_id, todo_id, new_todo)
    else: 
        flash('Enter something first to update')
    return redirect(url_for('home'))


@app.route('/todos/update_status/<todo_id>/<int:todo_status>')
@login_required
def update_todo_status_view(todo_id, todo_status):
    user_id = current_user.id
    update_todo_status_db(user_id, todo_id, todo_status)
    return redirect(url_for('home'))


@app.errorhandler(404)
def not_fount(error):
    return render_template('404.html', error= error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/hi')
def index():
    raise(Exception('500 error'))


if __name__=="__main__":
    app.run()