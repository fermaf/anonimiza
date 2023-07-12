# anonimiza
Anonimiza datos personales. MML analiza sistematicamente texto (ej. en documentos  públicos del Estado)  y anonimiza según normativa de protección a datos personales. Así:
* El Estado no tiene pretexto para cumplir con que sus actos son públicos (por regla general).
* Las personas siempre recibirán inforamación del Estado.
* El Estado se moderniza🤩 (empieza a hacerse eficiente (hasta que sea inecesario 🤘🔥✅)
  
Utilizando herramientas mágicas :) HuggingsFace, Langchain para gestionar LLM (Large Lenguaje Models) como OpenAI, se podría solucionar si de de forma abastracta hacer una planificación cognicitiva de,  con tareas jerarquerizadas (o no), razonar en como resolverlo.


...En este doc, de acá en adelantees, será una AI la que escribe mayopritariamente.


## Introducción

En la era digital actual, la protección de los datos personales se ha convertido en una preocupación primordial. Este ebook tiene como objetivo proporcionar una guía sobre cómo utilizar las herramientas de Modelos de Lenguaje de Aprendizaje Automático (LLMs) gestionadas por Langchain y OpenAI para anonimizar datos personales en documentos PDF, de acuerdo con la normativa vigente en Chile sobre protección de datos personales.

## Conceptos clave

*Datos personales: Cualquier información que se refiere a una persona física identificada o identificable.

*Anonimización: Proceso de eliminación o alteración de datos personales de tal manera que la persona a la que se refieren no pueda ser identificada.

*Pseudonimización: Proceso de reemplazo de datos personales con pseudónimos o identificadores que no revelan la identidad de la persona a la que se refieren.

*Normativa de protección de datos en Chile: Conjunto de leyes y regulaciones que rigen la recopilación, almacenamiento, uso y divulgación de datos personales en Chile.

*Descripción de las herramientas de LLMs

Las herramientas de LLMs gestionadas por Langchain y OpenAI son sistemas de inteligencia artificial que pueden entender, generar y traducir texto en lenguaje natural. Estas herramientas pueden ser entrenadas para realizar una variedad de tareas, incluyendo la identificación y anonimización de datos personales en documentos de texto.

## Proceso de anonimización de datos

El proceso de anonimización de datos personales en documentos PDF utilizando las herramientas de LLMs incluye los siguientes pasos:

* Carga del documento PDF en la herramienta de LLM.
* Identificación de los datos personales en el documento utilizando el modelo de lenguaje.
* Anonimización de los datos identificados, ya sea eliminándolos o reemplazándolos con pseudónimos.
* Verificación de que todos los datos personales han sido correctamente anonimizados.
* Consideraciones legales y éticas

Es importante tener en cuenta las leyes y regulaciones de protección de datos en Chile al anonimizar datos personales. Además, también es crucial considerar las implicaciones éticas de la anonimización de datos, como el respeto a la privacidad y la confidencialidad.

## Conclusión y próximos pasos

## Referencias y recursos adicionales

Para obtener más información sobre la anonimización de datos y la protección de datos personales, se pueden consultar:
* Constitución 
* LEY 21096 Firma electrónica CONSAGRA EL DERECHO A PROTECCIÓN DE LOS DATOS PERSONALES https://www.bcn.cl/leychile/navegar?idNorma=1119730
* LEY 19628 SOBRE PROTECCION DE LA VIDA PRIVADA https://www.bcn.cl/leychile/navegar?idNorma=141599&idParte=8642700&idVersion=2020-08-26
* 
* LEY 20285 SOBRE ACCESO A LA INFORMACIÓN PÚBLICA https://www.bcn.cl/leychile/navegar?idNorma=276363]

# El código.

##Revisar:
Hay casos de uso del estudio de Langchain que pueden ser utilizados en el código

* Modificar salida (Ejemplo 3: de https://claude.ai/chat/07 ... db)
Este callback modifica el texto generado antes de devolverlo, por ejemplo para filtrar palabras inapropiadas:

python

<code> from langchain.callbacks.base import BaseCallbackManager

 class OutputModifier(BaseCallbackManager):
     def on_call_finish(self, fn_name, output):
         return output.replace("palabra_prohibidaXD", "[censurado]")

 callback_manager = OutputModifier()
 llm.add_callback_manager(callback_manager)
 Cualquier ocurrencia de "palabra_prohibidaXD" será reemplazada por "[censurado]" en la salida final.

<code>
