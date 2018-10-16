## Apuntes ddsi

### Entidad/Relación
Libros - Autores
"Los libros son un tipo de entidad" - Está mal usar "son". Nosotros elegimos como modelar. Pueden modelarse como una entidad pero no tienen por qué serla.

#### Teorema del Modelaje:
"El modelo cuanto más simple mejor"

Por eso a la hora de elegir entre poner por ejemplo fecha como entidad o como atributo de una relación, elegimos el atributo porque son lo mismo y simplifica el modelo.

Hay algunas restricciones sobre los atributos que no podemos reflejar en el diagrama, por lo que se adjunta una lista de restricciones que nos aseguraremos de que se cumplan en el código, por ejemplo una edad mínima para los autores.

#### Dependencia existencial
para que algo sea dependencia existencial tiene que ocurrir que forzosamente haya que identificar previamente que el otro exista

para que exista una persona tienen que existir sus padres, pero para identificar a una persona NO hay que identificar a sus padres. para identificar un asiento de un avión si que hay que identificar el avión. en la dependencia existencial lo importante es la IDENTIFICACIÓN y no la existencialidad

Una entidad no puede ser fuerte y débil a la vez, pero una entidad débil puede depender de otra que a su vez sea débil. por ejemplo si tenemos  


 [A]-a,x  
  |  
  |  
[[B]]-b,y  
  |  
  |  
[[C]]-c,z  

las claves serían A(__a__,x), B(__a,b__,y), C(__a,b,c__,z)



#### Entidad débil vs. Subtipo

una entidad débil B que depende de A, necesita ser identificada la A para poder identificar a B. Sin embargo, si es un subtipo simplemente indica que B es parte de A, pero B puede existir por si sola. Es decir, siendo una entidad débil, B necesita A, pero siendo un subtipo, B es parte de A.


Ejemplos:

(x,y)
Participación, cardinalidad.

(1,n): Puede tener muchas pero al menos tiene una.
(0,n): Puede tener muchas o ninguna
(1,1): Únicamente tiene 1


[Empleado]----< Trabaja > (Fecha)----[Departamento]


Si añado cardinalidades y después atributos tengo que recalcular porque cambian las cardinalidades.

Para escribir en el flujo de la derecha, tapo el flujo y la entidad de la dcha y leo: Un empleado en una fecha completa, ¿En cuantos dptos trabaja? --> en 1
En un dpto, en una fecha concreta, cuantos empleados hay? --> 1
Luego la cardinalidad es 1-1.


Ejemplo2

[Cliente] (1,1)---- < tiene > ---- (0,n) [vehículo]

Proceso: Tapamos el flujo de la dcha y leemos: ¿Un cliente cuántos vehículos tiene?
(0,n) puede tener muchos o uno

Tapamos el flujo de la izda y leemos: ¿Un vehículo cuántos clientes tiene?
(1,1) Un vehículo tiene que pertenecer a un cliente


Principios de usar agregaciones (unir varias entidades): Simplicidad
Se leen: "Un par trabajador-salario"
        "Una tripleta...."



####Ciclos

El uso de ciclos es usual
