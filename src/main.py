from app import create_app
from app.firestore_service import add_todo
from app.firestore_service import delete_todo
from app.firestore_service import get_todos
from app.firestore_service import update_todo
from flask_login import login_required
from flask import render_template
from flask import request
from flask import session


app = create_app()


@app.route("/", methods=['GET'])
@login_required
def home():

    user_ip = request.remote_addr
    context = {
        "saludo": "Hello word",
        "despedida": "bye"
    }
    
    auth = 1

    if auth:
        return render_template('home.html', **context, user_ip=user_ip)
    else:
        return render_template('home-no-auth.html')


if __name__=="__main__":
    app.run()