FROM python:3.7-slim-stretch

#RUN useradd --user-group --create-home --shell /bin/false app 
  
ENV HOME=/home/manage

WORKDIR $HOME/vivi5

ADD requirements.txt $HOME/vivi5/

ADD . $HOME/vivi5/

RUN pip install -r requirements.txt

#USER app