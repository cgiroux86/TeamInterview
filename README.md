# TeamInterview

**Docker Commands**

1.  create a docker image by running:

**docker build -t teaminterview-dev:latest .**

a) create container by running:**docker run --name ti-container --env-file=.env -p 5000:5000 teaminterview-dev**

b) run db migrations by running in container: **docker exec ti-container python3 manage.py db migrate**

c) copy migrations from container to host machine by running: **docker cp ti-container:/TeamInterview/migrations ~/path/to/host/destination**

2. Whenever rerunning container, to persist and save migrations for source control run docker container by bind mounting the host migrations folder created in step 1c by running: **docker run -it --name ti-container -v ~/pathFrom1C/migrations:/TeamInterview/migrations --env-file=.env ti**
<!-- 1. In docker container run:
   **docker exec ti-container python3 manage.py db init**
3. Create volume for migrations by running:
   **docker volume create teaminterview-dev**
4. whenever rerunning container, use command from 1a. -->
