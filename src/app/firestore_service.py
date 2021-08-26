from google.cloud import firestore


db = firestore.Client(project='todo-app-321822')


#USERS (C,R,U,D)

def add_user(new_user, password):
    """ 
        :param new_user: name of new user
        :type new_user: string
        :type password: string
    """
    db.collection('users').document(new_user).set({"password": password})


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def delete_user(user_id):
    db.document(f'users/{user_id}').delete()


#TO DO (C,R,U,D)

def add_todo(user_id, description):
    todos_collection_ref = db.collection('users')\
        .document(user_id).collection('todos')

    todos_collection_ref.add({
        "description" : description,
        "todo_status" : False
    })


def get_todos(user_id):
    todos = db.collection('users').document(user_id).collection('todos').get()
    return todos


def update_todo(user_id, todo_id, new_data):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({
        "description": new_data
    })


def update_todo_status_db(user_id, todo_id, todo_status):
    todo_status = not bool(todo_status)    #Change the current value of todo_status
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({
         "todo_status" : todo_status 
    })


def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()


def _get_todo_ref(user_id, todo_id):
    todo_ref = db.collection('users').document(user_id)\
        .collection('todos').document(todo_id)
    return todo_ref