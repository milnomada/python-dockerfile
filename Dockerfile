FROM python:3

ADD main.py /
RUN pip install flask
RUN PATH=PATH:/usr/bin
RUN ls -la /usr
RUN echo $PATH
RUN which python

CMD ["python", "./main.py"]