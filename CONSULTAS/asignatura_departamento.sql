SELECT cod_asignatura cod_asig, nombre_asignatura nombre
FROM asignatura_pregrado, departamento_academico
WHERE substring(cod_asignatura from 1 for 2)=siglas_depto
AND siglas_depto='CI';
