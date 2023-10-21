FROM python:3.9

# create directory for the app user
RUN mkdir -p /web

# create the appropriate directories
ENV HOME=/
ENV APP_HOME=/web
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod

COPY . .
RUN pip install -r requirements.txt
CMD python manage.py collectstatic

EXPOSE 8000
