import random 
import operator

class Evento:

    def __init__(self,nombre, hora_inicio_hora_fin):

        self.nombre = nombre
        self.hora_inicio, self.hora_fin = hora_inicio_hora_fin


class EventoExclusivo:

    def __init__(self,nombre,hora_inicio_hora_fin,cupo):

        self.nombre = nombre
        self.hora_inicio, self.hora_fin = hora_inicio_hora_fin
        self.cupo = cupo


class Administrar:

    def __init__(self):

        self.cupos = {}
        self.diccionario_de_asistentes_por_eventos = {} 

    def asignar_asistentes(self, lista_de_asistentes, lista_de_eventos):

        asistentes = lista_de_asistentes
        random.shuffle(asistentes)

        for x in asistentes:
            self.asignar_eventos(x,eventos)
            print(x, "tiene asignados los nombres de los siguientes eventos: ", self.lista_con_eventos)
        
        print(self.totales_en_diccionario(self.diccionario_de_asistentes_por_eventos)) 

    def asignar_eventos(self, un_asistente, lista_de_eventos):

        self.un_asistente = un_asistente
        self.lista_con_eventos = []
        self.lista_con_horas_ocupadas = []
        self.diccionario_con_eventos = {}

        eventos = lista_de_eventos
        random.shuffle(eventos)

        for y in eventos:

            horas = list(range(y.hora_inicio,y.hora_fin))

            if type(y) is Evento and (self.verificar_horas(horas,self.lista_con_horas_ocupadas)):

                for w in range(y.hora_inicio, y.hora_fin):
                        self.lista_con_horas_ocupadas.append(w)
                
                self.diccionario_con_eventos[y.nombre] = y.hora_inicio

                if y.nombre in self.diccionario_de_asistentes_por_eventos:
                    self.diccionario_de_asistentes_por_eventos[y.nombre] = self.diccionario_de_asistentes_por_eventos[y.nombre] + [self.un_asistente]
                elif y.nombre not in self.diccionario_de_asistentes_por_eventos:
                    self.diccionario_de_asistentes_por_eventos[y.nombre] = ([self.un_asistente])

            elif type(y) is EventoExclusivo and (self.verificar_horas(horas,self.lista_con_horas_ocupadas)):

                if y.nombre not in self.cupos:

                    for w in range(y.hora_inicio, y.hora_fin):
                            self.lista_con_horas_ocupadas.append(w)

                    self.cupos[y.nombre] = y.cupo - 1
                    self.diccionario_con_eventos[y.nombre] = y.hora_inicio

                    if y.nombre in self.diccionario_de_asistentes_por_eventos:
                        self.diccionario_de_asistentes_por_eventos[y.nombre] = (self.diccionario_de_asistentes_por_eventos[y.nombre] + [self.un_asistente])
                    elif y.nombre not in self.diccionario_de_asistentes_por_eventos:
                        self.diccionario_de_asistentes_por_eventos[y.nombre] = ([self.un_asistente])

                elif y.nombre in self.cupos and self.cupos[y.nombre] > 0:

                    for w in range(y.hora_inicio, y.hora_fin):
                            self.lista_con_horas_ocupadas.append(w)

                    self.cupos[y.nombre] = self.cupos.get(y.nombre) - 1
                    self.diccionario_con_eventos[y.nombre] = y.hora_inicio

                    if y.nombre in self.diccionario_de_asistentes_por_eventos:
                        self.diccionario_de_asistentes_por_eventos[y.nombre] = (self.diccionario_de_asistentes_por_eventos[y.nombre] + [self.un_asistente])
                    elif y.nombre not in self.diccionario_de_asistentes_por_eventos:
                        self.diccionario_de_asistentes_por_eventos[y.nombre] = ([self.un_asistente])

        self.lista_con_eventos = self.ordenar_eventos(self.diccionario_con_eventos)
          
    """Verifica las horas para que el asistente no tenga
    imcompatibilidad  de horario"""

    def verificar_horas(self,lista_uno,lista_dos): 

        for x in lista_uno:
            if x in lista_dos:
                return False 

        return True
    
    """Ordena los eventos a modo de guia para el 
    asistente"""   

    def ordenar_eventos(self,diccionario_con_eventos):

        self.lista = []
        diccionario_sort = sorted(diccionario_con_eventos.items(), key = operator.itemgetter(1),
        reverse=False)

        for nombre in enumerate(diccionario_sort):
            self.lista.append(nombre[1][0])
       
        return self.lista

    """Agrega los totales al diccionario de eventos"""
    
    def totales_en_diccionario(self, diccionario):
        self.diccionario = diccionario
        for x in self.diccionario:
            cantidad = 0
            for y in self.diccionario[x]:
                cantidad = cantidad + 1
            self.diccionario[x] = (self.diccionario[x], cantidad)
        return diccionario


if __name__ == "__main__":
    asistentes = ["Luciano", "Julian", "Lucas", "Martín"]
    eventos = [EventoExclusivo("Capitán América",(10,13),2), EventoExclusivo("Hulk",(10,11),1),
    EventoExclusivo("Los 4 fantásticos",(11,12),3),EventoExclusivo("Mujer Maravilla",(13,14),2), Evento("Hombre araña",(16,17))]
    prueba = Administrar()
    prueba.asignar_asistentes(asistentes,eventos)
    


