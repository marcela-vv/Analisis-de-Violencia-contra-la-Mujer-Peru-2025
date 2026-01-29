# Analisis-de-Violencia-contra-la-Mujer-Peru-2025
Análisis de datos y scraping de denuncias del SIDPOL (Mininter) para monitorear la evolución de la violencia contra la mujer en el Perú durante el 2025.


**1. Descripción del proyecto**

Este proyecto realiza un análisis exploratorio de datos públicos sobre denuncias de violencia contra la mujer en el Perú, con el objetivo de identificar patrones territoriales y variaciones porcentuales entre años recientes. A partir de técnicas básicas de web scraping, limpieza y análisis de datos en Python, se busca aportar una lectura comunicacional que permita comprender cómo se distribuye y evoluciona el fenómeno a nivel departamental.

**2. Pregunta de investigación**


¿Qué departamentos han mostrado el mayor crecimiento porcentual (aceleración) de denuncias en el último año?


**3. Fuente de datos**


Observatorio Nacional de Seguridad Ciudadana del Ministerio del Interior


**4. Metodología**

Obtención de datos

Se descargaron datos públicos del Observatorio Nacional de Seguridad Ciudadana mediante técnicas de web scraping y/o descarga directa de archivos CSV, asegurando que la información corresponda a denuncias registradas oficialmente.

Limpieza y preparación de datos

Los datos fueron procesados en Python para:

    - eliminar valores nulos o inconsistentes,

    - estandarizar nombres de departamentos,

    - organizar la información por año y territorio.

Procesamiento y análisis


Se agruparon las denuncias por departamento y se calculó la variación porcentual interanual, con el fin de identificar qué territorios presentan mayores cambios relativos en el número de denuncias.

Análisis comunicacional


Los resultados se interpretaron desde una perspectiva social y comunicacional, considerando que las variaciones en las denuncias pueden reflejar tanto cambios reales en la violencia como modificaciones en los niveles de denuncia, acceso institucional o visibilidad del problema.



**5. Principalez hallazgos**

En un contexto donde el registro nacional de 2025 muestra una caída generalizada, Tumbes, Ica y Lambayeque emergen como los departamentos con la mayor “aceleración” relativa. Las regiones mencionadas fueron las que menos descendieron en sus cifras (caídas de solo -41% frente al -58% de otras regiones). Aquello sugiere que mantienen una tasa de ingreso de denuncias más constante que el resto del país.

Marzo es consistentemente el mes con el pico más alto de denuncias (promedio histórico de 304,000 incidentes), superando largamente a junio, que suele ser el mes más “templado” (promedio de 267,000). 

Enero acumula 270,367 denuncias: la cifra más alta del 2025 hasta la fecha. A partir de febrero, la curva muestra un descenso abrupto mes a mes. La violencia no ha desaparecido, pero la capacidad del sistema para procesar y publicar la data en tiempo real se va degradando conforme avanza el año. 

Lima Metropolitana, Arequipa y Cusco registran la mayor cantidad de casos; no obstante, cuando se analiza el crecimiento, Tumbes pasa del puesto 20 en volumen al 1, e Ica del 7 al 2. Esto muestra que, pese a las cifras absolutas de Lima, Tumbes e Ica presentan una proporción de actividad superior. Huancavelica y Madre de Dios registran el menor volumen de denuncias, con menos de 11,000 casos en 2025. Moquegua presenta cifras bajas y una reducción del 58%, lo que indica un descenso en el registro de conflictos.

