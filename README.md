# ProyectoPipelineBTC

## Descripción de la actividad:
En esta actividad, los estudiantes deberán diseñar e implementar un pipeline con 5 filtros para procesar una transacción de compra de Bitcoin (BTC) usando distintas monedas base (USD, EUR o GBP).

El objetivo es comprender cómo los patrones arquitectónicos de tipo pipeline permiten estructurar un flujo de procesamiento en etapas secuenciales, cada una con responsabilidades bien definidas, promoviendo la separación de preocupaciones, la reutilización y la mantenibilidad del código.

Cada filtro representará una etapa específica del procesamiento de una transacción y deberá implementarse como un módulo independiente, comunicándose con el siguiente a través de una interfaz común.

# Requisitos del pipeline:

## Filtro de Validación:
Verifica que la transacción contenga los datos obligatorios:

ID del usuario

Monto de BTC

Moneda base (USD, EUR o GBP)

## Filtro de Autenticación:
Confirma la identidad del usuario mediante una verificación contra una base de datos o sistema simulado (puede ser un JSON local o una función mock que represente RDS).

## Filtro de Transformación:
Convierte el valor de BTC a la moneda base utilizando una API REST (puede usarse una API pública o un servicio simulado con datos fijos).

## Filtro de Cálculo de Comisiones:
Calcula la comisión fija de la transacción (por ejemplo, 5.00 USD o su equivalente en la moneda base) y la agrega al total procesado.

## Filtro de Almacenamiento:
Guarda la transacción procesada en una base de datos (SQLite, archivo JSON o cualquier otro método persistente).
