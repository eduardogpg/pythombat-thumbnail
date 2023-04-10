def download_image(medifile_uri, localpath):
    import requests
    
    try:
        response = requests.get(medifile_uri, stream=True)
        if response.status_code == 200:
            
            with open(localpath, 'wb') as file:
                
                for chunk in response:
                    file.write(chunk)

        print('Imagen descargada!')
    except Exception as err:
        print(err)

IMAGES = [
    {
        'name': 'expresiones-regulares-python-pt2',
        'uri': 'https://i.imgur.com/EoLrT9D.png'
    },
    {
        'name': 'realmente-conoces-los-strings',
        'uri': 'https://i.imgur.com/dOW1cXb.png'
    },
    {
        'name': 'funciones-anonimas-python',
        'uri': 'https://i.imgur.com/rNYQkZC.png'
    },
    {
        'name': 'interpolacion-python',
        'uri': 'https://i.imgur.com/IfRoWw0.png'
    },
    {
        'name': 'expresiones-regulares-python-pt3',
        'uri': 'https://i.imgur.com/t7kkgHZ.png'
    },
    {
        'name': 'ejecucion-automatica-scripts-python',
        'uri': 'https://i.imgur.com/f3czmai.png'
    },
    {
        'name': 'patrones-expresiones-regulares',
        'uri': 'https://i.imgur.com/VdCQGem.png'
    },
    {
        'name': 'generadores-python-pt2',
        'uri': 'https://i.imgur.com/LMxysEl.png'
    },
    {
        'name': 'como-testear-aplicaciones-python',
        'uri': 'https://i.imgur.com/Ce5BQk3.png'
    },
    {
        'name': 'aplicacion-tiempo-real-python',
        'uri': 'https://i.imgur.com/QP6QjLD.png'
    },
    {
        'name': 'mainipuacion-sistema-python',
        'uri': 'https://i.imgur.com/IH69bEo.png'
    },
    {
        'name': 'middleware-django',
        'uri': 'https://i.imgur.com/pKY3E9H.png'
    },
    {
        'name': 'CLI-python',
        'uri': 'https://i.imgur.com/djH0Qja.png'
    },
    {
        'name': 'generadores-python',
        'uri': 'https://i.imgur.com/WvcPzl2.png'
    },
    {
        'name': 'interfaz-linea-comandos',
        'uri': 'https://i.imgur.com/kjI0Dhd.png'
    },
    {
        'name': 'expresiones-regulares-python',
        'uri': 'https://i.imgur.com/ef4dwab.png'
    },
    {
        'name': 'concer-mi-version-python',
        'uri': 'https://i.imgur.com/gDLWfXy.png'
    },
    {
        'name': 'data-classes',
        'uri': 'https://i.imgur.com/KcIQ3em.png'
    },
    {
        'name': 'strings-python',
        'uri': 'https://i.imgur.com/XwsMfx3.png'
    },
]

if __name__ == '__main__':
    
    for image in IMAGES:
        download_image(image['uri'], f'tmp/images/{image['name']}.png')
        
        Id Leer objeto
        Sí

        Grupo
        Leer objeto