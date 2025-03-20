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

## Ejemplo de uso

```
# python graphQLConverter.py '{"query": "{ me { name } }"}'
```

