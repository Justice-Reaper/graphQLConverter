# GraphQLConverter

Este script convierte un JSON de GraphQL en un formato x-www-form-urlencoded, que es comúnmente utilizado en solicitudes HTTP con el Content-Type: application/x-www-form-urlencoded. Además, limpia el JSON de caracteres innecesarios (como saltos de línea, tabulaciones y espacios múltiples) para garantizar que la cadena resultante sea válida y esté optimizada para su uso en solicitudes web

## Características principales

1. **Conversión de JSON a URL-encoded**:
   - Transforma un objeto JSON de GraphQL (que incluye query, operationName y variables) en una cadena codificada para su uso en solicitudes HTTP

2. **Limpieza de JSON**:
   - Elimina caracteres innecesarios como saltos de línea (\n), tabulaciones (\t), espacios múltiples y otros caracteres de control que podrían afectar la validez del JSON

3. **Fácil de usar**:
   - El script se ejecuta desde la línea de comandos y acepta el JSON como argumento
   - Proporciona un panel de ayuda (-h) para guiar al usuario en su uso

4. **Robusto**:
   - Valida el JSON de entrada y muestra un mensaje de error claro si el JSON no es válido
   - Maneja argumentos adicionales y muestra la ayuda si se detectan errores en los argumentos

## Panel de ayuda

```
# python graphql_converter.py -h
usage: graphql_converter.py [-h] [json]

Convert a GraphQL JSON to URL encoded format

positional arguments:
  json        GraphQL JSON as a string. Example: '{"query": "{ me { name } }"}'

options:
  -h, --help  show this help message and exit

Example: python graphql_converter.py '{"query": "{ me { name } }"}'
```

## Ejemplo de uso

```
# python GraphQLConverter.py '{"query":"\n    mutation changeEmail($input: ChangeEmailInput!) {\n        changeEmail(input: $input) {\n            email\n        }\n    }\n","operationName":"changeEmail","variables":{"input":{"email":"testing@gmail.com"}}}'
URL Encoded Data:
query=mutation+changeEmail%28%24input%3A+ChangeEmailInput%21%29+%7BchangeEmail%28input%3A+%24input%29+%7Bemail%7D%7D&operationName=changeEmail&variables=%7B%22input%22%3A+%7B%22email%22%3A+%22testing%40gmail.com%22%7D%7D
```
