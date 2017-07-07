SELECT cod_asignatura, cod_depto, nombre_depto
FROM asignatura_pregrado, departamento_academico
WHERE substring(cod_asignatura from 1 for 2)=siglas_depto
AND cod_asignatura='MA1111';
