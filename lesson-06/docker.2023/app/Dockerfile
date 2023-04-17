FROM ubuntu:22.10

RUN apt update && apt install -y cowsay fortune

RUN mkdir /app
ADD run.sh /app/

WORKDIR /app/

ENTRYPOINT ["bash", "/app/run.sh"]
