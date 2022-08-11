FROM alpine:latest
USER root
RUN apk update && apk add python3 socat
WORKDIR /task
COPY ./conv.py /task/conv.py
COPY ./flag.txt /task/flag.txt
ENTRYPOINT ["socat"]
CMD ["TCP-LISTEN:4444,fork,reuseaddr", "EXEC:'timeout 120 python3 /task/conv.py',stderr"]
EXPOSE 4444
