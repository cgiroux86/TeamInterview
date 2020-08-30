# TeamInterview

# Docker Commands

    docker run  --env-file=.env  -p 5000:5000 --mount source=teaminterview,target=/app teaminterview
    docker volume create teaminterview
