docker image build -t pytadahdtentity:latest .
docker container run  --interactive --env CODECOV_TOKEN=$CODECOV_TOKEN --tty --rm --name pytadahdtentity pytadahdtentity:latest

