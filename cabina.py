class Cabina:
    def __init__(self, codice_cabina, num_letti, ponte, prezzo_base):
        self.codice_cabina = codice_cabina
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo_base = prezzo_base
        self.occupata = False

    def prezzo_finale(self):
        return self.prezzo_base

    def __str__(self):
        stato = "Occupata" if self.occupata else "Disponibile"
        return f'{self.codice_cabina}: | {self.num_letti} letti - ponte {self.ponte} - prezzo {self.prezzo_finale():.2f}€ - la cabina è {stato}'

class Cabine_animali(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo_base, max_animali):
        super().__init__(codice_cabina, num_letti, ponte, prezzo_base)
        self.max_animali = max_animali

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.10 * self.max_animali)

    def __str__(self):
        stato = "Occupata" if self.occupata else "Disponibile"
        return f'{self.codice_cabina}: | {self.num_letti} letti - ponte {self.ponte} - prezzo {self.prezzo_finale():.2f}€ - la cabina è {stato}'

class Cabina_deluxe(Cabina):
    def __init__(self, codice_cabina, num_letti, ponte, prezzo_base, caratteristica):
        super().__init__(codice_cabina, num_letti, ponte, prezzo_base)
        self.caratteristica = caratteristica

    def prezzo_finale(self):
        return self.prezzo_base * 1.20

    def __str__(self):
        stato = "Occupata" if self.occupata else "Disponibile"
        return f'{self.codice_cabina}: | {self.num_letti} letti - ponte {self.ponte} - prezzo {self.prezzo_finale():.2f}€ - la cabina è {stato}'


