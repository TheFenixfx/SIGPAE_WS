# Base de datos para los webservices de SIGPAE
#
# En primer lugar es necesario ingresar a PostgreSQL como administrador
# $ sudo -su postgres
# $ psql
#
# Luego de esto crearemos un usuario nuevo y una base de datos nueva.
#
# $ create user sigpae with password '123123';
# $ create database dacepregrado with owner sigpae;
#
# Se utilizó la herramiento pgfutter disponible en: https://github.com/lukasmartinelli/pgfutter

# Variables de entorno, cambiar si es necesario de acuerdo a la base de datos creada
export dbname=dacepregrado
export user=sigpae
export pass=LXHyCmFD9rQPCqC
export schema=public
export PGPASSWORD=$pass

psql -U sigpae -d dacepregrado -f droptable.sql
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/ASIGNATURA_PREGRADO.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/ASIGNATURA_PREGRADO_HISTORIA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/CARRERA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/CARRERA_ELECTIVA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/CARRERA_OBLIGATORIA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/CB_ASIGNATURA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/DEPARTAMENTO_ACADEMICO.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/ESTUDIANTE.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/ESTUDIANTE_ASIGNATURA.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/PERIODO_USB.csv -d ";"
./pgfutter --db $dbname --schema $schema --user $user --pw $pass csv CSV/COORDINACION_CARRERA.csv -d ";"
