FROM python:3.11.0rc2-bullseye

#WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask pyodbc


COPY . .

CMD [ "python", "./frontend.py" ]

#acceder data base en docker como postgres:
#docker exec -it postgres-test psql -U postgres

