FROM python:3.8 as base

# to skip generating bytecode files within the container, it help to redunce container size
ENV PYTHONDONTWRITEBYTECODE 1
# to ensure that Python output is sent directly to the console
ENV PYTHONUNBUFFERED 1

# expose port where the app will run
EXPOSE 9000

# It allows you to create multiple build stages within a single Dockerfile,
# each with its own base image and set of instructions.
# also use to optimize the final size of the resulting Docker image and
# separate the build environment from the runtime environment.
FROM base as build

# create a directory in container
RUN mkdir /kollabhunt
WORKDIR /kollabhunt/kollabhunt_backend

# install dependencies
RUN pip install --upgrade pip

# Copy source code & libraries
COPY ["/kollabhunt-packages", "/kollabhunt/kollabhunt_backend/kollabhunt-packages/"]
COPY ["/kollabhunt/kollabhunt_backend", "/kollabhunt/kollabhunt_backend/"]

# Copy dependencies file to container working directory
COPY ["./kollabhunt/requirements.txt", "/kollabhunt/kollabhunt_backend"]

# run command to install packages
RUN pip install -r requirements.txt
RUN pip install -e kollabhunt-packages

RUN mkdir /kollabhunt/static
RUN python manage.py collectstatic --no-input

# run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
