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

Note: Before starting with these steps make sure to run the docker-compose.yml in your machine if you are in a development environment.

Requirements:
* you must have a Heroku account, this will be used to deploy our app. (This because this application was done to be deployed on this platform)
* Also you must have an account of Google Cloud Platform, this will be required to use the Firestore service (our database).

Steps:

1. Once you have cloned this repository you will need one file named `KeyFile.json`, this file must contain the credentials that the app needs to authenticate with the Firestore service. Then, you just need to put it inside the **/config** directory.

    * (only for **production environment**) --> To can add the KeyFile.json to Git, you have to delete this line in the .gitignore file:

        `
        config/*
        `

        **IMPORTANT**: I recommend you add the credentials file in another branch different to the main branch, only for security, and then to push it to Heroku.
    
    How to get the credentials?

    To get these credentials you will need to create a key file linked to one service account, you can read about it [here](https://cloud.google.com/docs/authentication/getting-started).

2. (This step is only for **production environment**) Once you are in Heroku CLI you have to set the following environment variable that flask needs to work. 

    Type this command:

    ```bash
    heroku config:set SECRET_KEY_FLASK="6enuJsmM2tatuhUN7vjpKmYfcvrsrCvDvGGxSS4eAqV4dSq9ZxVGUudSQNF27jNk"
    ```

    Make sure that the secret key is secure (and don't use the same of above) 

\
**Note**: When you want to run the app in the development environment just type:

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
