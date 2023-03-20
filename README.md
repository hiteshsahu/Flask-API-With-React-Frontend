# Building Flask API with Docker ⚗️
> ### Python backend using Python3 Flask With Docker

----

## **SETUP** ⚙️

Set up python venv

    python3 -m venv venv
    Set-ExecutionPolicy Unrestricted
    .\venv\Scripts\activate

Install Flask

    pip3 install python-dotenv
    pip3 install flask



-----

## **BUILD** 🏗️


MacOS:

    export FLASK_APP=flaskr
    export FLASK_ENV=development

Windows:

    set FLASK_APP=flaskr
    set FLASK_ENV=development

Start Front end

> npm start

Start API server via cmd prompt

> cd api

> python3 -m flask  run

OR use npm to start API
>  npm run start-api


- API will start on **http://127.0.0.1:5000**

- React App will start on **http://localhost:3000/**


Debug Run

    flask --app flaskr --debug run

Non debug run

      flask --app flaskr --no-debugger


## **DEPLOYMENT** 📦

Build Docker Container Image 
 
    docker build --tag python-docker .

Validate Image is created

    docker images

Result:

    (venv) D:\GitHub\Flask-API>docker images
    REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
    python-docker   latest    199cf8a5350c   4 minutes ago    145MB

Run Container with flask

    docker run -d -p 5000:5000 python-docker

Result:
    
    (venv) D:\GitHub\Flask-API>docker ps
    CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                    NAMES
    df3f37944e57   python-docker   "flask --app flaskr …"   3 minutes ago   Up 3 minutes   0.0.0.0:5000->5000/tcp   jovial_joliot


Reference:
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Official Docker Document for Python](https://docs.docker.com/language/python/)
- [Containerize an application](https://docs.docker.com/get-started/02_our_app/)
