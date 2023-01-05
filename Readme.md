Welcome to my trabajo for pancho
================================

-> Crear la RED #em este caso: panchosred
```
docker network create panchosred
```

# Levantar la base de datos

->Para levantar la DB hay que hacer
```
docker run --name db -e POSTGRES_PASSWORD=1234 --net=panchosred -p 5432:5432 -it -d postgres:14
```
    #-Para ejecutar una consola de postgres como Usuario postgres
    ```
    docker exec -it db psql -U postgres
    ```

        #si no levanta por el uso de los puertos: listar si el puerto esta en uso
        ```
        sudo lsof -i -P -n | grep LISTEN
        ```
        #depende que servicio tiene en uso el puerto, matarlo
        ```
        pidof postgres | en el caso que sea postgres el servicio. esto lista que pid usa postgres
        ```
        #luego: 
        ```
        sudo kill 1330 1329 1328 1318 1317 1219 | son los num de servicio que usa postgres
        ```

->Para levantar el python que ayuda a desarrolar
```
docker run -it --name backend --net=panchosred python:3.11.0rc2-bullseye # --hostname backend --alias backend 
```

    -y en otro terminal, mientras aquel esta abierto:
    ```
    docker exec -it backend pip install psycopg2-binary
    ```
