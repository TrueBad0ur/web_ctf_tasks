FROM alpine:latest
USER root
RUN apk update && apk add python3 py3-pip
RUN pip3 install flask 
RUN adduser -S hacker
USER hacker
COPY ./flag.txt /home/hacker/flag.txt
COPY ./templates /home/hacker/templates
COPY ./appl.py /home/hacker/appl.py
USER root
RUN chmod 500 /home/hacker
RUN chown hacker /home/hacker/templates/index.html
USER hacker
WORKDIR /home/hacker
ENTRYPOINT ["python3"]
CMD ["/home/hacker/appl.py"]
#CMD ["python3", "appl.py"]
EXPOSE 31338
