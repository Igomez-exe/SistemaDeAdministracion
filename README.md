# SistemaDeAdministracion

Consigna : 

Se necesita un sistema para administrar los eventos de una convención de cómics que se realizará el próximo año. Se dispone, para ello, de una lista de eventos 
(charlas, cosplay, performance, concursos, etc) y de asistentes.De los eventos se tiene el nombre, y la hora de inicio y de fin, también pueden existir eventos exclusivos 
del cual ademas de los datos anteriores se le agrega el cupo  (cantidad de personas admitidas). De los asistentes, solamente los nombres de fantasía. 
Varios eventos ocurren al mismo tiempo, o con horarios parcialmente solapados.

Se sabe que todos los asistentes irán a tantos eventos como puedan ir, pero por cuestiones de organización y espacio deberemos asignarlos mediante un programa 
desarrollado a tal fin.Este programa deberá mezclar los asistentes, mezclar los eventos, y asignarle eventos a cada asistente hasta que no pueda ser asignado a más eventos 
por incompatibilidad de horario. ¡Cuidado con los cupos de los eventos que los tengan!Se debe repetir hasta llenar los horarios de todos los asistentes,
o hasta terminar con los cupos disponibles.

El programa debe arrojar un listado de asistentes por evento (individuos y totales) y un listado de eventos por asistente (ordenados por horario) a modo de guía para cada 
participante.

Ejemplo : 

       - asistentes=["Luciano", "Julian", "Lucas", "Martín"]
       
       - eventos = [EventoExclusivo("Capitán América",(10,13),2), EventoExclusivo("Hulk",(10,11),1),
         EventoExclusivo("Los 4 fantásticos",(11,12),3),EventoExclusivo("Mujer Maravilla",(13,14),2), Evento("Hombre araña",(16,17))]
         
       
       Salida del programa : 
                            - Luciano tiene asignados los nombres de los siguientes eventos: "Capitán América", "Mujer Maravilla", "Hombre araña"
                            - Julian tiene asignados los nombres de los siguientes eventos: "Capitán América", "Mujer Maravilla", "Hombre araña"
                            - Lucas tiene asignados los nombres de los siguientes eventos: "Hulk", "Los 4 fantásticos", "Hombre araña"
                            - Martín tiene asignados los nombres de los siguientes eventos: "Los 4 fantásticos", "Hombre araña"
                            
                            - {"Capitán América": (["Julian", "Luciano"],2), "Hulk": (["Lucas"],1), "Los 4 fantásticos": (["Martín"],1), 
                              "Mujer Maravilla": (["Luciano","Julian"],2), "Hombre araña": (["Martín", "Luciano","Julian","Lucas" ],4)}
