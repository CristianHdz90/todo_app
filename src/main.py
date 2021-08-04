from flask import render_template, request
from app import create_app
from app.firestore_service import get_users

app = create_app()

@app.route("/")
@app.route("/home")
def home():

    user_ip = request.remote_addr
    
    #To get users
    users = get_users()
    print(users)

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