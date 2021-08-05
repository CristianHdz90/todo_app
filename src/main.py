from flask import render_template, request
from app import create_app
#CRUD of users
from app.firestore_service import add_user, get_user, delete_user
#CRUD of to-do's
from app.firestore_service import add_todo, get_todos, update_todo, delete_todo


app = create_app()

@app.route("/")
@app.route("/home", methods=['GET'])
def home():

    user_ip = request.remote_addr
    
    #Adding to-do's
    
    # todo = {
    #     'task 2':'xxxxxx'
    # }
    # add_todo('camilo', todo)

    #Get todos
    # get =  get_todos('camilo')
    # for i in get:
    #     print(i.to_dict())

    #Update todo #
    # update_todo('camilo', 'lRyK6Ze0Buz4hCJcGyF2', {'descriptio': 'xxxxxxx'})

    #Delete todo
    # delete_todo('camilo', 'JjBDZf8BZB0yEOlfJIVG')




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