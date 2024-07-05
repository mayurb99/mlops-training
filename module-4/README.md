1) Running script via docker to store the artifact to s3
-> Create file .env.aws and add AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID
-> run command docker run --env-file .env.aws  < image-name > < year > < month >

2) To create pip env in multiple folders 

-> run export PIPENV_IGNORE_VIRTUALENVS=1
-> run pipenv install < packages >
-> run pipenv shell