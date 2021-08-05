from google.cloud import firestore


db = firestore.Client(project='todo-app-321822')


#USERS (C,R,U,D)

def add_user(new_user, data):
    db.collection('users').document(new_user).set(data)


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def delete_user(user_id):
    db.document(f'users/{user_id}').delete()

     


#TO DO (C,R,U,D)

def add_todo(user_id, todo):
    todo_ref = db.collection('users').document(user_id).collection('todos')
    todo_ref.add(todo)


def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()


def update_todo(user_id, todo_id, new_data):
    db.collection('users').document(user_id).collection('todos').document(todo_id).update(new_data)


def delete_todo(user_id, todo_id):
    db.collection('users').document(user_id).collection('todos').document(todo_id).delete()