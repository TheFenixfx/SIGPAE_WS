SELECT ap.cod_asignatura, ap.nombre_asignatura nombre
FROM asignatura_pregrado ap, estudiante_asignatura ea 
WHERE ea.anio_carnet='11' 
AND ea.nro_carnet='10199' 
AND ea.cod_asignatura=ap.cod_asignatura
AND ea.nota_asignatura IN ('3','4','5');
