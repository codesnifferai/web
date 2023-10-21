#Copy to codesnifferai/Dockerfile
FROM python:3.9

COPY . .
# create the appropriate directories
ENV HOME=/
ENV APP_HOME=/web
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod

RUN pip install -r requirements.txt
CMD python manage.py collectstatic

EXPOSE 8000
