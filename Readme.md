Welcome to my trabajo for pancho
================================

-> Crear la RED #en este caso: backendNET & frontendNET
```
docker network create backendNET
```
```
docker network create frontendNET
```

# Levantar la base de datos

->Para levantar la DB hay que hacer
```
docker run --name db -e POSTGRES_PASSWORD=1234 --net=backendNET -p 5432:5432 -it -d postgres:14
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

->Para levantar el python que ayuda a desarrolar el backend
```
docker run -it --name backend --net=backendNET python:3.11.0rc2-bullseye
```

    -y en otro terminal, mientras aquel esta abierto:
    ```
    docker exec -it backend pip install psycopg2-binary
    ```
    

->Para levantar el python que ayuda a desarrolar frontend    
    
```
docker run -it --name frontend --net=frontendNET python:3.11.0rc2-bullseye
```
    -y en otro terminal, mientras aquel esta abierto:
    ```
    docker exec -it frontend pip install flask
    ```
