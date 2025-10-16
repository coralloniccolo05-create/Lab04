class Cabina:
    def __init__(self, codice_cabina, num_letti, ponte, prezzo):
        self.codice_cabina = codice_cabina
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = prezzo

class Cabine_animali(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo, max_animali):
        super().__init__(codice_cabina, num_letti, ponte, prezzo)
        self.max_animali = max_animali

class Cabina_deluxe(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo, caratteristica):
        super().__init__(codice_cabina, num_letti, ponte, prezzo)
        self.caratteristica = caratteristica
