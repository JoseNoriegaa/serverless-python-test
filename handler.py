from requests import get

# INEGI API path params
LATITUDE = 29.072968
LONGITUDE = -110.955917
CONDITION = 'todos'
BASE_URL = 'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscar'
METERS = 500
TOKEN = '<YOUR API KEY>'

def hello(event, context):

    try:
        # Obtiene los establecimientos de Hermosillo, Sonora.
        response = get(f'https://www.inegi.org.mx/app/api/denue/v1/consulta/buscar/{CONDITION}/{LATITUDE},{LONGITUDE}/{METERS}/{TOKEN}')
    except:
        response = '[]'

    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": response.text
    }
