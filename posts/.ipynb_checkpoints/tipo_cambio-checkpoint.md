---
title: Filtrando los Tipos de Cambios al final de cada mes (Nicaragua) con Python
slug: tipo_cambios_python
tags: Python
date: 2019-10-18 22:26:00 UTC
---

En este post vamos a trabajar los tipos de cambios que publica el Banco Central de Nicaragua.

Por medio de Python podemos filtrar la fecha de tipo de cambios que deseamos. Algo que en excel sería mucho trabajo pero en Python con unas pocas lineas podemos hacerlo.

¿Cómo obtenemos los tipos de cambios? Los encontramos en este enlace del banco central. [Enlace](https://www.bcn.gob.ni/estadisticas/mercados_cambiarios/tipo_cambio/cordoba_dolar/index.php) . 

<!-- TEASER_END -->

### Obteniendo los tipos de cambios.

Al dirigirnos a la dirección del enlace podemos seleccionar un rango de fechas para escoger los tipos de cambios que nos interesa.

![undefined](https://i.pinimg.com/originals/44/cc/18/44cc18fb9d8f4b2763cfe7081fd366e1.png)

* Seleccionando "Rango de fechas"
* Elegir fecha inicial y fecha final
* Descargar el archivo de Excel.

En este ejercicio la fecha elegidas son 1 de Enero de 2000 y 31 de Octubre de 2019. El objetivo de este ejercicio es obtener el tipo de cambio de final de cada mes entre esas fechas seleccionadas.

Una vez damos clic en el ícono de Excel, se descarga el archivo. Por motivo de elaborar este ejercicio lo he subido al servidor de driver y haremos el llamado desde python. Si el archivo ya no se encuentra disponible favor escribirme. [Descargar](https://drive.google.com/open?id=1yV8heEHIzzFwR-2nYbPZp4owNqmUin2z) . Ha sido guardado manualmente con extensión .xlsx.

El archivo abierto desde excel contiene lo que se ve en la imagen:

![undefined](https://i.pinimg.com/originals/9d/42/e6/9d42e630e1de626c7f8db4869b79e97e.png)

Primera columna son las fechas y la segunda columna contiene los tipos de cambio. ¿Cuánto córdobas se pagaría por 1 dólar estadounidense?

Podríamos aplicar filtro y seleccionar los finales de cada mes pero eso sería muy tedioso tachar fecha por fecha. También podriamos utilizar PowerQuery o quizás Tabla dinámica pero yo utilizaré la libreria Pandas de Python.

Primero debemos importar pandas.

```python
import pandas as pd
```

Proseguimos a extraer los datos del archivo de Excel

```python
excel = pd.read_excel(r'C:\Users\JENNY\Google Drive\Datos\BLOG_PERSONAL\Archivo.xlsx', sheetname=0, 
              skiprows = 6)
```

El argumento sheetname es para seleccionar la hoja en la que se encuentra los datos. En python todo comienza a contarse desde 0. Por eso la hoja 1 en excel sería la 0 en python.

Habíamos visto que en el excel está el logo del banco central y varias filas que no nos interesa. Los datos empiezan desde la fila 7. Por tal razón skiprows es 6. }

Haciendo uso de un excel.head(), podemos observar parte de los datos.

```python
Fecha	Córdobas por USD
0	01-January-00	12.3202
1	02-January-00	12.3222
2	03-January-00	12.3242
3	04-January-00	12.3261
4	05-January-00	12.3281
```

Si queremos saber qué hemos importado, podemos usar un excel.info()

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7192 entries, 0 to 7191
Data columns (total 2 columns):
Fecha               7192 non-null object
Córdobas por USD    7192 non-null float64
dtypes: float64(1), object(1)
memory usage: 112.4+ KB
```

Recibimos información de que tenemos 7192 filas de datos distribuídas en dos columnas.
Además podemos notar que tenemos una Fecha pero como objeto. Pero los tipos de cambios están en formato correcto, es decir en float. Por último también observamos que no tenemos valores perdidos.

Convirtamos la columna Fecha a verdaderamente fecha.

```python
excel.loc[:,'Fecha'] = excel.loc[:,'Fecha'].apply(pd.to_datetime) 
```
Con la rutina anterior hemos convertido a fechas de python.

Podemos confirmar aplicando info() de nuevo.

```python
excel.info()
```

```python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7192 entries, 0 to 7191
Data columns (total 2 columns):
Fecha               7192 non-null datetime64[ns]
Córdobas por USD    7192 non-null float64
dtypes: datetime64[ns](1), float64(1)
memory usage: 112.4 KB
```

Ya vemos que Fecha es datetime, el formato de fecha de python.

Muchas empresas solo necesitan el tipo de cambio del último día del mes. Por tal razón nos interesará dejar solo esos tipos de cambios y omitir el resto de días. Haremos un filtro automatizado para 7,192 datos.

```python
tipo_cambio = excel.groupby(pd.Grouper(key='Fecha', freq='1M')).last()
```

Notemos que key es la columna de fechas. Freq se refiere a agrupar en una frecuencia, en este caso mensual. Last() va presentar el último tipo de cambio de la agrupación. En muchas empresas pueden preferir un promedio mensual, para esto tendrían que sustituir last() por mean(). 

Veamos los datos con tail.

```python
tipo_cambio.tail()
```

```python
	Córdobas por USD
Fecha	
2019-06-30	33.1222
2019-07-31	33.2598
2019-08-31	33.3979
2019-09-30	33.5321
2019-10-31	33.6713
```

Podemos ver que tenemos de cada mes el último día con su respectivo tipo de cambio.

Si quisieramos conocer el tipo de cambio del 31 de agosto del 2019 podemos filtra con loc.

```python
tipo_cambio.loc['2019-08-31']
```

```python
Córdobas por USD    33.3979
Name: 2019-08-31 00:00:00, dtype: float64
```

O de un año específico, por ejemplo del 2013.

```python
tipo_cambio.loc['2013-01-31' : '2013-12-31']
```

```python
Córdobas por USD
Fecha	
2013-01-31	24.2257
2013-02-28	24.3165
2013-03-31	24.4175
2013-04-30	24.5156
2013-05-31	24.6174
2013-06-30	24.7163
2013-07-31	24.8190
2013-08-31	24.9220
2013-09-30	25.0222
2013-10-31	25.1261
2013-11-30	25.2270
2013-12-31	25.3318
```

El intervalo se separa con **:**.

Con un simple gráfico podriamos ver la evolución del tipo de cambio.

```python
from matplotlib import pyplot as plt
%matplotlib inline
plt.plot(tipo_cambio)
plt.show()
```

![undefined](https://i.pinimg.com/originals/b6/9d/46/b69d4640de8839532ffd7dbb245033fe.png)

Ya podemos dar por terminado este post.

***Cualquier duda puede consultar a morales.economia@gmail.com***

