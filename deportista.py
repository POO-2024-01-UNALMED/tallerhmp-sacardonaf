class Deportista:
    def __init__(self, deporte="Futbol", años=0):
        self._deporte=deporte
        self._añosPracticando=años

    def getDeporte(self):
        return self._deporte

    def setDeporte(self,deporte):
        self._deporte=deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self, años):
        self._añosPracticando=años