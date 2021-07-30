from flask import render_template
from app import create_app

app = create_app()

@app.route("/")
@app.route("/home")
def home():

    context = {
        "saludo": "Hello word",
        "despedida": "bye"
    }
    
    auth = 1

    #IF está AUTH mostrar (UserHome) else show (inicio) 

    if auth:
        return render_template('home.html', **context)
    else:
        return render_template('home-no-auth.html')



if __name__=="__main__":
    app.run()