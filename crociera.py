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
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) == 4:
                        codice_cabina, num_letti, ponte, prezzo = row
                        cabina = Cabina(codice_cabina, int(num_letti), int(ponte), int(prezzo))
                        self.lista_cabine.append(cabina)
                    elif len(row) == 5 and len(row[4]) == 1:
                        codice_cabina, num_letti, ponte, prezzo, max_animali =  row
                        cabina_animali = Cabine_animali(codice_cabina, int(num_letti), int(ponte), int(prezzo), int(max_animali))
                        self.lista_passeggeri.append(cabina_animali)
                    elif len(row) == 5 and len(row[4]) != 1:
                        codice_cabina, num_letti, ponte, prezzo, caratteristica = row
                        cabina_deluxe = Cabina_deluxe(codice_cabina, int(num_letti), int(ponte), int(prezzo),caratteristica)
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

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO



