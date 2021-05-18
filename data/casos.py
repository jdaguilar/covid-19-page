import pandas as pd
import requests

base_url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"


def get_json_response(base_url, params):
    r = requests.get(url = base_url, params = params)
    data = r.json()
    return data


def get_total_casos():
    df = get_total_acumulado()
    penultimate_day, last_day = df.tail(2).acumulado.values

    return last_day, penultimate_day


def get_total_recuperados():
    params = {
        "$select": "COUNT(*) as total_casos_confirmados",
        "$where": "Recuperado = 'Recuperado'",
    }
    casos_recuperados = get_json_response(base_url, params)[0]["total_casos_confirmados"]
    casos_recuperados = int(casos_recuperados)

    return casos_recuperados


def get_total_fallecidos():
    params = {
        "$select": "COUNT(*) as total_casos_confirmados",
        "$where": "Estado = 'Fallecido'",
    }
    casos_fallecidos = get_json_response(base_url, params)[0]["total_casos_confirmados"]
    casos_fallecidos = int(casos_fallecidos)

    return casos_fallecidos


def get_total_casos_activos():
    params = {
        "$select": "COUNT(*) as total_casos_confirmados",
        "$where": "Recuperado = 'Activo'",
    }
    casos_activos = get_json_response(base_url, params)[0]["total_casos_confirmados"]
    casos_activos = int(casos_activos)

    return casos_activos


def get_distribucion_por_genero():

    params = {
        "$select": "UPPER(sexo) as Sexo, COUNT(id_de_caso) as cantidad",
        "$group": "UPPER(sexo)",
    }
    casos_activos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos_activos)

    return df


def get_edades():

    params = {
        "$select": "edad, COUNT(id_de_caso) as cantidad",
        "$group": "edad",
    }
    casos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos)

    return df


def get_distribucion_por_departamento():

    params = {
        "$select": "departamento as codigo, departamento_nom as nombre, COUNT(id_de_caso) as cantidad",
        "$group": "codigo, nombre",
        "$order": "cantidad DESC",
    }
    casos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos)

    df['codigo'] = df['codigo'].replace({
        '5':'05',
        '8':'08',
        '8001':'08',
        '13001':'13',
        '47001':'47',
    })

    df['nombre'] = df['nombre'].replace({
        'BARRANQUILLA':'ATLANTICO',
        'CARTAGENA':'BOLIVAR',
        'STA MARTA D.E.':'MAGDALENA',
    })

    df['cantidad'] = df['cantidad'].astype(int)

    df = df.groupby(by=['codigo','nombre']).sum()
    df = df.reset_index()
    df = df.sort_values(by=['cantidad'],ascending=False)

    return df


def get_acumulado_fallecidos():

    params = {
        "$select": "fecha_muerte as fecha, COUNT(id_de_caso) as cantidad",
        "$where": "fecha_muerte IS NOT NULL AND Estado = 'Fallecido'",
        "$group": "fecha",
    }
    casos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos)
    df['fecha'] = pd.to_datetime(df['fecha'],dayfirst=True)
    df['cantidad'] = pd.to_numeric(df['cantidad'])
    df = df.sort_values('fecha')
    df['acumulado'] = df['cantidad'].cumsum()

    return df


def get_acumulado_recuperados():

    params = {
        "$select": "fecha_recuperado as fecha, COUNT(id_de_caso) as cantidad",
        "$where": "fecha_recuperado IS NOT NULL",
        "$group": "fecha",
    }
    casos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos)
    df['fecha'] = pd.to_datetime(df['fecha'],dayfirst=True)
    df['cantidad'] = pd.to_numeric(df['cantidad'])
    df = df.sort_values('fecha')
    df['acumulado'] = df['cantidad'].cumsum()

    return df


def get_total_acumulado():

    params = {
        "$select": "fecha_reporte_web as fecha, COUNT(id_de_caso) as cantidad",
        "$group": "fecha",
    }
    casos = get_json_response(base_url, params)
    df = pd.DataFrame.from_records(casos)
    df['fecha'] = pd.to_datetime(df['fecha'],dayfirst=True)
    df['cantidad'] = pd.to_numeric(df['cantidad'])
    df = df.sort_values('fecha')
    df['acumulado'] = df['cantidad'].cumsum()

    return df
