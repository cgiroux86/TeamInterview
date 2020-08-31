# TeamInterview

# Docker Commands

    1) create a docker image by running: docker build -t teaminterview-dev:latest .
        a) create container by running:
       docker run --name ti-container --env-file=.env  -p 5000:5000 --mount source=teaminterview-dev,target=/TeamInterview teaminterview-dev

    1) In docker container run: docker exec ti-container python3 manage.py init
    2) Create volume for migrations by running: docker volume create teaminterview-dev
    3) whenever rerunning container, use command from 1a.
