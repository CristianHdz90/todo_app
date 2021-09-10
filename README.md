# Todo App

This responsive application will allow you to note your pending tasks when you please.

## Functionality

1. Login
2. Create and Delete your account.
3. Create, Update and Delete tasks.
4. Save the current state of your tasks (done or to do).

And the best, ¡You might use it from any device!

### Technologies

* Flask
* Python :snake:
* Docker :whale2:
* Html
* Css
* Heroku
* Bootstrap
* Firestore
* GoogleCloudSDK

---
## How to use it in production and development

Note: Before starting with these steps you have to run the docker-compose.yml in your machine if you are in a development environment or the heroku.yml on the Heroku platform if you want to start the app in production.

Requirements:
* you must have a Heroku account, this will be used to deploy our app. (This because I've done this application to be deployed on this platform)
* Also you must have an account of Google Cloud Platform, this will be required to use the Firestore service (our database).

Steps:

*This first step is only for **production environment***

1. First of all you have to set the following environment variable that flask needs to work. 

    *Bash example*:
    ```bash
    export SECRET_KEY_FLASK="uALZuZSksQLeQ4@&_%EwHakWke_Fm-=^3=cqxUC@U+VQc!W7tEp_6Pm?6@+wZJ-UR"
    ```
    Make sure that the secret key is secure (and don't use the same of above)

2. Now you will need one file named `KeyFile.json`, this file must contain the credentials for the app to connect it to the Firestore service. Then, you just need to put it in the **/config** directory.

    How to get the credentials?

    To get these credentials you will need to create a key file linked to one service account, you can read about it [here](https://cloud.google.com/docs/authentication/getting-started).

3. Once the above is done, you just need to set the next environment variable that contains the route to the credentials file to authenticate your app with Firestore.

    *Bash example*:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/todo_app/config/KeyFile.json"
    ```

    Note: If you're in the development environment you have to call the application with the 5000 port, e.g.

    ```bash
    flask run -h 0.0.0.0 -p 5000 
    ```

---
## Gallery

1.  #### Home without authentication
    \
    ![home_no_auth](https://raw.githubusercontent.com/CristianHdz90/todo_app/main/src/app/static/images/gallery/home_no_auth.png "home no auth")


2. #### Log in page
    \
    ![login](https://raw.githubusercontent.com/CristianHdz90/todo_app/main/src/app/static/images/gallery/login.png "login page")

3. #### Sign up page
    \
    ![signup](https://raw.githubusercontent.com/CristianHdz90/todo_app/main/src/app/static/images/gallery/signup.png "signup page")

4. #### Home
    \
    ![home](https://raw.githubusercontent.com/CristianHdz90/todo_app/main/src/app/static/images/gallery/home.png "main home")

---
### Created by:

[@CristianHdz90](https://linktr.ee/CristianHdz90 "About cristianhzd90")
