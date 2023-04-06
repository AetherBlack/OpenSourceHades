
FROM debian:stable

EXPOSE 80

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-pip gcc make build-essential

COPY ./src/requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "/app/hades.py" ]
