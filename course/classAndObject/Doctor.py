class Doctor:
    def studied_years(self):
        print("i studied 7 years")
    def paid_by_who(self):
        print("i get paid by the governemet")

class FamilyDoctor(Doctor):
    def paid_by_who(self):
        print("i get paid by the people")