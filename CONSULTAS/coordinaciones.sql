SELECT DISTINCT nombre_coordinacion nombre, email_coordinacion email
FROM coordinacion_carrera coord, carrera carr
WHERE carr.cod_carrera = coord.cod_carrera AND nombre_coordinacion != ''
ORDER BY nombre_coordinacion