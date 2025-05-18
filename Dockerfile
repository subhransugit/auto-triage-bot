FROM ubuntu:latest
LABEL authors="subhr"

ENTRYPOINT ["top", "-b"]
