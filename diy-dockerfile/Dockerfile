# Base image to build
FROM python:3.12-rc-bullseye

# Work directory specific to web IDE
# You can change if you are running on your
# Local Machine
WORKDIR /exercise_2

# COPY requirements.txt to container before
# Running the code
# This way any change in requirements will affect only 
# one layer.
COPY requirements.txt requirements.txt

# Install required libraries
RUN pip install -r requirements.txt

# Add code file to container directory.
ADD . .

# Running the code file
# You can also use ENTRYPOINT here.
CMD [ "python", "date_time.py" ]