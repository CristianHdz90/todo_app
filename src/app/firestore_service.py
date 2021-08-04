from google.cloud import firestore

db = firestore.Client(project='todo-app-321822')

#USERS


#In order to get users
def get_users():
    return db.collection('users').get()


#TO DOS

def get_todos():
    pass
