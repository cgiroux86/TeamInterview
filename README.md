# TeamInterview

# Docker Commands

    docker run  --env-file=.env --name ti-container  -p 5000:5000 --mount source=teaminterview,target=/app teaminterview
    docker volume create teaminterview
