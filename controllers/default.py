# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import re

@request.restful()
def webservices():
    def GET(*args, **vars):
        response = []
        if len(args) <= 0:
            return []
        if args[0] == 'carreras':
            response = carreras()                     #/carreras
        elif args[0] == 'estudiantes':
            if len(args) > 1:
                if args[1] == 'asig-aprobadas':
                    if 'carnet' in vars.keys():
                        response = asig_aprobadas(vars['carnet']) #/estudiantes/asignaturas-aprob?carnet=
                    else:
                        raise HTTP(400)
            else:
                if 'carnet' in vars.keys():
                    response = estudiante_carnet(vars['carnet']) #/estudiantes?carnet=
                elif 'cedula' in vars.keys():
                    response = estudiante_cedula(vars['cedula']) #/estudiantes?cedula=
                else:
                    raise HTTP(400)
        elif args[0] == 'asignaturas':
            if len(args) > 1:                          #/asignaturas/CI2125
                response = asignatura(args[1])
            else:
                response = lista_asignaturas(vars)     #/asignaturas
        elif args[0] == 'departamentos':
            response = departamentos()                 #/departamentos
        else:
            raise HTTP(404)

        return response

    def POST(*args, **vars):
        return dict()

    def PUT(*args, **vars):
        return dict()

    def DELETE(*args, **vars):
        return dict()

    return locals()

## /carreras
def carreras():
    query = db.executesql("SELECT cod_carrera, nombre_carrera nombre, tipo_carrera tipo FROM carrera", as_dict=True)
    return response.json(query)

## /estudiantes?carnet=11-10199
def estudiante_carnet(carnet):
    if not re.match('^[0-9]{2}-[0-9]{5}', carnet):  # Chequear que el carnet tenga formato 11-10199
        raise HTTP(400)
    lista = carnet.split("-")      # Carnet en formato 01-12345
    lista[0] = str(int(lista[0]))  # Quitar cero al inicio
    query = db.executesql(
        '''SELECT 
             cedula_estudiante ci, 
             nombres_estudiante nombres, 
             apellidos_estudiante apellidos,
             estado_civil,
             sexo
           FROM estudiante
           WHERE anio_carnet=%s AND nro_carnet=%s''', lista, as_dict=True)
    return response.json(query)

# /estudiantes?cedula=23625373
def estudiante_cedula(cedula):
    query = db.executesql(
        '''SELECT 
             cedula_estudiante ci, 
             nombres_estudiante nombres, 
             apellidos_estudiante apellidos,
             estado_civil,
             sexo
           FROM estudiante
           WHERE cedula_estudiante=%s''', [cedula], as_dict=True)
    return response.json(query)

# /estudiantes/asig-aprobadas?carnet=11-10199
def asig_aprobadas(carnet):
    lista = carnet.split("-")      # Carnet en formato 01-12345
    lista[0] = str(int(lista[0]))  # Quitar cero al inicio
    query = db.executesql(
        '''SELECT ap.cod_asignatura, ap.nombre_asignatura nombre
           FROM asignatura_pregrado ap, estudiante_asignatura ea 
           WHERE ea.anio_carnet=%s 
           AND ea.nro_carnet=%s 
           AND ea.cod_asignatura=ap.cod_asignatura
           AND ea.nota_asignatura IN ('3','4','5');''', lista, as_dict=True
    )
    return response.json(query)

def asignatura(cod_asignatura):
    query = db.executesql(
        '''SELECT 
             cod_asignatura, 
             nombre_asignatura nombre, 
             nro_creditos creditos, 
             nro_horas_teoria h_teoria,
             nro_horas_practica h_practica,
             nro_horas_laboratorio h_laboratorio,
             anio_periodo_desde vig_desde,
             anio_periodo_hasta vig_hasta
           FROM asignatura_pregrado
           WHERE cod_asignatura=%s''', [cod_asignatura], as_dict=True
    )
    return response.json(query)

def lista_asignaturas(vars):
    query = []
    # Asignaturas asociadas a un departamento
    if vars.get('siglas_depto'):
        query = db.executesql(
            '''SELECT cod_asignatura, nombre_asignatura nombre
               FROM asignatura_pregrado, departamento_academico
               WHERE substring(cod_asignatura from 1 for 2)=siglas_depto
               AND siglas_depto=%s''', [vars.get('siglas_depto')], as_dict=True
        )

    #Asignaturas asociadas a una carrera
    elif vars.get('cod_carrera'):
        cod_carrera = str(vars.get('cod_carrera'))
        query = db.executesql(
            '''SELECT asig.cod_asignatura, nombre_asignatura nombre, 'O' as tipo
               FROM carrera_obligatoria oblig, asignatura_pregrado asig
               WHERE oblig.cod_carrera=%s
               AND asig.cod_asignatura=oblig.cod_asignatura
               UNION
               SELECT asig.cod_asignatura, nombre_asignatura, 'E' as tipo
               FROM carrera_electiva elec, asignatura_pregrado asig
               WHERE elec.cod_carrera=%s
               AND asig.cod_asignatura=elec.cod_asignatura
               ORDER BY tipo DESC, cod_asignatura''', [cod_carrera,cod_carrera], as_dict=True
        )

    else:
        query = db.executesql(
            '''SELECT cod_asignatura, nombre_asignatura nombre
               FROM asignatura_pregrado''', as_dict=True
        )
    return response.json(query)

# /departamentos
def departamentos():
    query = db.executesql(
        '''SELECT cod_depto, nombre_depto nombre, siglas_depto, e_mail_depto email
           FROM departamento_academico
           WHERE nombre_depto NOT IN ('DESCONOCIDO', 'SIN DEFINIR')''', as_dict=True
    )
    return response.json(query)