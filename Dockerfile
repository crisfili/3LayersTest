FROM python:3.11.0rc2-bullseye

#WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

EXPOSE 5000

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]