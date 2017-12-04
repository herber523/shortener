FROM python:3.6.3

ENV PROJ_DIR /shortener
ADD . $PROJ_DIR 
WORKDIR $PROJ_DIR
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
