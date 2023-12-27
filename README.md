# Docker-service

---- before run server please sure you have install docker on your pc ----

---- check that docker service is running and active ----


first install requirements with `pip install -r requirements.txt`

then fill `.env`file with your actual postgres database info or uncomment DATABASE with sqllite and 

use sqlite instead 

then run thiese commands 

`python manage.py makemigrations`
`python manage.py migrate `

 at the end run `python manage.py runserver `

 now you can use endpoints but please make sure that import correct data 
 
 for post and put  request it must be dict for this endpoint `/crud-docker-app/create-app`
 
 and its must be list for this rndpoint `/run-docker-app/`
 
 tnx !!!
