FROM python:3.5

EXPOSE 8000

# Install system dependencies for python
RUN apt-get update
RUN apt-get install -y libpq-dev python-dev gcc g++ libxslt-dev libtiff5-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
                        liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
ENV LIBRARY_PATH=/lib:/usr/lib

# Install NPM
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get -y install nodejs

WORKDIR /app

# Install assets
COPY package.json /app/package.json
RUN npm install

# Install PIP packages
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Copy the app and define volumes
COPY . /app
VOLUME /app/staticfiles

# Define the run script
RUN chmod +x /app/bash/run-prod.sh
CMD /app/bash/run-prod.sh