SELECT asig.cod_asignatura, nombre_asignatura, 'obligatoria' as tipo
FROM carrera_obligatoria oblig, asignatura_pregrado asig
WHERE oblig.cod_carrera='0800'
AND asig.cod_asignatura = oblig.cod_asignatura
UNION
SELECT asig.cod_asignatura, nombre_asignatura, 'electiva' as tipo
FROM carrera_electiva elec, asignatura_pregrado asig
WHERE elec.cod_carrera='0800'
AND asig.cod_asignatura = elec.cod_asignatura
ORDER BY tipo DESC, cod_asignatura;