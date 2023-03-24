class FajlokFledolgozasa:
    def __init__(self, sor):
        daraboltTisztitottSor = sor.strip().split(";")
        self.nev = daraboltTisztitottSor[0]
        self.jelszo = daraboltTisztitottSor[1]
        self.email = daraboltTisztitottSor[2]

    def __str__(self):
        return f"Név: {self.nev}, jelszó: {self.nev}, email: {self.nev}."
