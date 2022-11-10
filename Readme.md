Welcome to my trabajo for pancho
================================

# TODO: Poneme una seccion de como crear la red.

```
docker network create...
```

# Levantar la base de datos

->Para levantar la DB hay que hacer
```
docker run --name db -e POSTGRES_PASSWORD=1234 --net=panchosred -p 5432:5432 -it -d postgres:14 # --alias db --hostname db
```

    #-Para ejecutar una consola de postgres como Usuario postgres
    #```
    #docker exec -it db psql -U postgres
    #```

->Para levantar el python que ayuda a desarrolar
```
docker run -it --name backend --net=panchosred python:3.11.0rc2-bullseye # --hostname backend --alias backend 
```

-y en otro terminal, mientras aquel esta abierto:
```
docker exec -it backend pip install psycopg2-binary
```
