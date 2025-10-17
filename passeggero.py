class Passeggero:
    def __init__(self, codice_passeggero, nome, cognome):
        self.codice_passeggero = codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.cabina = None

        def __str__(self):
            info_cabina = f" - Cabina: {self.cabina.codice}" if self.cabina else " - Nessuna cabina assegnata"
            return f'{self.codice_passeggero} {self.nome} {self.cognome}'