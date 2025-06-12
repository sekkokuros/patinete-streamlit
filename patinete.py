
class PatineteEletrico:
    def __init__(self, modelo, autonomia_km, velocidade_max):
        self._modelo = modelo
        self._autonomia_km = autonomia_km
        self._velocidade_max = velocidade_max
        self._ligado = False

    def get_modelo(self):
        return self._modelo

    def get_autonomia_km(self):
        return self._autonomia_km

    def get_velocidade_max(self):
        return self._velocidade_max

    def esta_ligado(self):
        return self._ligado

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_autonomia_km(self, autonomia):
        self._autonomia_km = autonomia

    def set_velocidade_max(self, velocidade):
        self._velocidade_max = velocidade

    def ligar_patinete(self):
        if not self._ligado:
            self._ligado = True
            return "Patinete ligado com sucesso!"
        else:
            return "O patinete já está ligado."
