# SIGPAE_WS

## Instrucciones

Primero crearemos la base de datos en PostgreSQL

Ingresar a PostgreSQL
```bash
$ sudo -su postgres
$ psql
```
Crear el usuario y la base de datos si no existen en la consola de postgres. (El usuario y el password es el
mismo de SIGPAE)

```bash
$ create user sigpae with password '123123';
$ create database dacepregrado with owner sigpae;
```

**SIGPAE** y **SIGPAE WS** usan el mismo usuario y password. En la version de desarrollo (rama ```master```) y la versión de producción (rama ```deploy```) los passwords difieren.

Una vez realizado esto se ejecuta el script para cargar los archivos CSV a la base de datos.

```bash
$ ./cargar_datos.sh
```

### Nota
Si el usuario, contraseña y/o nombre de la base de datos es distinto, es necesario modificar el archivo
cargar_datos.sh con los valores apropiados.

```bash
export dbname=<nombre_bd>
export user=<usuario>
export pass=<password>
```
