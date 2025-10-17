from tkinter.font import names
import csv
from cabina import Cabina, Cabine_animali, Cabina_deluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.lista_cabine = []
        self.lista_passeggeri = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 4:
                        codice_cabina, num_letti, ponte, prezzo_base = row
                        cabina = Cabina(codice_cabina, int(num_letti), int(ponte), int(prezzo_base))
                        self.lista_cabine.append(cabina)
                    elif len(row) == 5 and len(row[4]) == 1:
                        codice_cabina, num_letti, ponte, prezzo_base, max_animali =  row
                        cabina_animali = Cabine_animali(codice_cabina, int(num_letti), int(ponte), float(prezzo_base), int(max_animali))
                        self.lista_cabine.append(cabina_animali)
                    elif len(row) == 5 and len(row[4]) != 1:
                        codice_cabina, num_letti, ponte, prezzo_base, caratteristica = row
                        cabina_deluxe = Cabina_deluxe(codice_cabina, int(num_letti), int(ponte), float(prezzo_base), caratteristica)
                        self.lista_cabine.append(cabina_deluxe)
                    elif len(row) == 3:
                        codice_passeggero, nome, cognome = row
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.lista_passeggeri.append(passeggero)

        except FileNotFoundError:
            raise Exception(f"File {file_path} non trovato.")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        cabina = None
        for cab in self.lista_cabine:       #scorro gli oggetti nella lista
            if cab.codice_cabina == codice_cabina:
                cabina = cab        #trovo la cabina con quel codice all'interno della mia lista di oggetti
                break

        if cabina is None:
            raise Exception("Cabina non trovata.")

        if cabina.occupata is True:
            raise Exception("Cabina già occupata.")

        for pas in self.lista_passeggeri:
            if pas.codice_passeggero == codice_passeggero:
                passeggero = pas

        if passeggero.cabina is not None:
            raise Exception("Passeggero già associato ad una cabina.")

        cabina.occupata = True      #rendo occupata la cabine con quel codice occupata
        passeggero.cabina = cabina  #dico che il passeggero adesso appartiene alla cabina


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        self.lista_cabine.sort(key=lambda cabine: cabine.prezzo_finale())
        return self.lista_cabine


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        if not self.lista_passeggeri:
            print("Nessun passeggero registrato.")
            return

        for passeggero in self.lista_passeggeri:
            if passeggero.cabina is None:
                print(f"{passeggero.codice_passeggero}: {passeggero.nome} {passeggero.cognome} - Nessuna cabina assegnata")
            else:
                print(f"{passeggero.codice_passeggero}: {passeggero.nome} {passeggero.cognome} - Cabina: {passeggero.cabina.codice_cabina}")

