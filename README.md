# Telepathology Django Backend

Telepathology-backend is Django REST APIs created to support a mini digital microscope that will help in remote pathology sample collection and reporting. Developed the application as MVP for early stage startup. As the startup no longer working on product, I have open source the project. 

## Technologies Used

Django, Django Rest Framework, PostgreSQL, Django ORM, Docker, Docker-compose, Heroku, AWS EC2, AWS S3, AWS RDS

## Telepathology Frontend Repository 
Telepathology Frontend Git Repo - https://github.com/shubhamrathi97/telepathology-frontend

Backend Deployed on Heroku and Frontend is deploy on Netlify. You can view the credential to login and preview application in frontend repository. 


## FEATURES

###### Django Modules

* Doctor
* Operator
* Images
* Pathology Sample
* User
* Address

###### Role Based Access

* Doctor
* Operator
* Admin

###### Operator can create Patient and upload images of patient's sample blood/stool/urine slide from microscope.

###### Doctor can review the Pathology Sample.

###### Image Uploads on AWS S3 via Presigned URL from frontend

###### Token Based Authentication

###### Sample can be uploaded in Image Batches

###### Doctor, Operator, Admin Registration and Login (Customize User Model)


## HOW TO RUN

1. Please set `DATABASE_URL` environment variable as Postgres DB URL. In case of any other Database, Please modify the database setting in `src/backend/settings.py` file.
2. Create Virtual environment, Activate it and execute `pip install -r requirements.txt`
3. Please create Migration by running `python src/manage.py makemigrations`
4. Please run the migration by running  `python src/manage.py migrate`
5. Execute `python src/manage.py runserver 0.0.0.0:8000`

## HEROKU DEPLOYMENT

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true

## DOCKER DEPLOYMENT

`docker-compose up`

If You need SSL, Kindly check the 'prod' branch for Letsencrypt added with Nginx in Docker Compose File.
