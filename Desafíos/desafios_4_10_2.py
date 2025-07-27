#Desafío 2: Cambio Frecuente en Requisitos
"""Supón que estás desarrollando un juego de video con distintos tipos de personajes y armas. 
Los requerimientos cambian con frecuencia, añadiendo nuevos personajes y habilidades. 
Mantener y actualizar TADs en este escenario podría ser una tarea titánica."""

class Personaje:
    def __init__(self, vida, stamina, mana, nivel):
        self.vida = vida
        self.stamina = stamina
        self.mana = mana
        self.nivel = nivel

    def __str__(self):
        return f"{self.__class__.__name__}(Vida: {self.vida}, Stamina: {self.stamina}, Mana: {self.mana}, Nivel: {self.nivel})"


class Mago(Personaje):
    def __init__(self, vida, stamina, mana, nivel, hechizos):
        super().__init__(vida, stamina, mana, nivel)
        self.hechizos = hechizos

    def __str__(self):
        base = super().__str__()
        return f"{base}, Hechizos: {self.hechizos}"


class Guerrero(Personaje):
    def __init__(self, vida, stamina, mana, nivel, armadura):
        super().__init__(vida, stamina, mana, nivel)
        self.armadura = armadura

    def __str__(self):
        base = super().__str__()
        return f"{base}, Armadura: {self.armadura}"

class Picaro(Personaje):
    def __init__(self, vida, stamina, mana, nivel, sigilo):
        super().__init__(vida, stamina, mana, nivel)
        self.sigilo = sigilo

    def __str__(self):
        base = super().__str__()
        return f"{base}, Sigilo: {self.sigilo}"

class Armas:
    def __init__(self, nombre, durabilidad, damage, nivel, tipo):
        self.nombre = nombre
        self.durabilidad = durabilidad
        self.damage = damage
        self.nivel = nivel
        self.tipo = tipo

    def __str__(self):
        return f"{self.__class__.__name__}(Nombre: {self.nombre}, Durabilidad: {self.durabilidad}, Damage: {self.damage}, Nivel: {self.nivel}, Tipo: {self.tipo})"
