# Recommender engine application
## Deployed here
https://misis-rec-sys.herokuapp.com

## Local development
#### Build docker image
docker build -t rec-sys .

#### Run docker image locally
docker run -d -p 5000:5000 --name recommendation-system rec-sys

## Heroku
#### login to container repository
heroku container:login

#### push image
heroku container:push web

#### release image
heroku container:release web

## Sample usage of prediction API
#### Get app health
curl https://misis-rec-sys.herokuapp.com/health

#### get users
curl https://misis-rec-sys.herokuapp.com/api/users | jq '.'

#### use popularity based predictions
curl -H 'Content-Type: application/json' https://misis-rec-sys.herokuapp.com/api/predictions -d '{"predictions_count": 7 }' | jq '.'

#### use collaborative filtering for predictions
curl -H 'Content-Type: application/json' https://misis-rec-sys.herokuapp.com/api/predictions -d '{"predictions_count": 7, "user_id": "Fiona Adams" }' | jq '.'
