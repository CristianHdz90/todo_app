from flask import render_template, request
from app import create_app
from flask_login import login_required
#CRUD of users
from app.firestore_service import add_user, get_user, get_users, delete_user
#CRUD of to-do's
from app.firestore_service import add_todo, get_todos, update_todo, delete_todo


app = create_app()


@app.route("/", methods=['GET'])
# @login_required
def home():

    user_ip = request.remote_addr
    context = {
        "saludo": "Hello word",
        "despedida": "bye"
    }
    

    # print(get_user('camilo').id)


    auth = 1

    if auth:
        return render_template('home.html', **context, user_ip=user_ip)
    else:
        return render_template('home-no-auth.html')


if __name__=="__main__":
    app.run()