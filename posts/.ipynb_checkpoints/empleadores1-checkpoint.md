---
title: Empleados Permanentes y Temporales del Sistema Bancario de Nicaragua en Junio 2019
slug: superintendencias_empleados
date: 2019-09-05 16:00:00 UTC
---

Empezamos con nuestro primer post panorámico de la economía de Nicaragua, con los cuales queremos ofrecer algunas estadísticas obtenidas de las fuentes oficiales.

Con la herramienta R y los datos de la Superintendencia de Bancos y de Otras Instituciones Financieras, he extraído la cantidad de empleados del sistema bancario.

Importando el json del servicio web de la SIBOIF y procesándolo con R, hemos obtenido lo siguiente:

<!-- TEASER_END -->

### Empleados Permanentes
```r
## # A tibble: 7 x 4
##   Institucion `2017-12-31` `2018-12-31` `2019-06-30`
##                                 
## 1 AVANZ                 NA          254          255
## 2 BAC                 2596         2205         2087
## 3 FICOHSA              529          614          587
## 4 BANCENTRO           2211         1894         1844
## 5 BANCORP              103          118           25
## 6 BANPRO              2473         2297         2107
## 7 BDF                 1034          922          518
```

La tabla generada en R revela que la crisis sociopolítica que afectó al país desde abril 2018 ha provocado despidos masivos en los bancos. Bancorp y Ficohsa contrataron personal permanente entre finales del 2017 y diciembre 2018. Pero en el primer semestre del 2019 el Bancorp despidió a 93 trabajadores.

Según los datos de la SIBOIF el BDF ha sido el banco que ha despedido hasta 404 trabajadores sólo en el primer semestre del 2019.

<iframe width="1000px" height="600px" src="https://fogadereportes.netlify.com/docs/p2.html" frameborder="0" allowfullscreen="" webkitallowfullscreen="" msallowfullscreen="">
<p>
Tu navegador no soporta esta vista, comunicarse con <a href="mailto:deybi.morales@fogade.gob.ni" class="email">deybi.morales@fogade.gob.ni</a>
</p>
</iframe>

### Empleados Temporales
```r
## # A tibble: 7 x 4
##   Institucion `2017-12-31` `2018-12-31` `2019-06-30`
##                                 
## 1 AVANZ                 NA            0            0
## 2 BAC                    0            0            0
## 3 FICOHSA                0            0            0
## 4 BANCENTRO              0            0            0
## 5 BANCORP                4            4           24
## 6 BANPRO                 5            3            0
## 7 BDF                    1            5            3
```

Los empleados temporales aumentaron en Bancorp, disminuyeron en BDF y Banpro.

Ahora sumaremos los dos cuadros para obtener el total de empleados por bancos.

### Empleados Totales

```r
##   Institucion 2017-12-31 2018-12-31 2019-06-30
## 1       AVANZ         NA        254        255
## 2         BAC       2596       2205       2087
## 3     FICOHSA        529        614        587
## 4   BANCENTRO       2211       1894       1844
## 5     BANCORP        107        122         49
## 6      BANPRO       2478       2300       2107
## 7         BDF       1035        927        521
```

Con la ayuda de Plotly podemos elaborar bellas gráficas interactivas:

<iframe width="1000px" height="600px" src="https://fogadereportes.netlify.com/docs/p1.html" frameborder="0" allowfullscreen="" webkitallowfullscreen="" msallowfullscreen="">
<p>
Tu navegador no soporta esta vista, comunicarse con <a href="mailto:deybi.morales@fogade.gob.ni" class="email">deybi.morales@fogade.gob.ni</a>
</p>
</iframe>

Solo Avanz ha mantenido casi constante el número de empleados contratando uno más con respecto a diciembre 2018. Pero Ficohsa ha sido el único banco que ha aumentado su planilla de empleados según los datos del periodo observado, 58 más con respecto a finales del 2017.

En conclusión, sin tomar en cuenta a Avanz, el sistema bancario ha despedido a 1,761 trabajadores. Este nivel tan negativo puede ser causa del impacto financiero de la crisis sociopolítica que inició en el primer semestre del año 2018.
