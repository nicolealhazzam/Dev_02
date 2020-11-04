class Date:
	__init__(s, jour, mois, annee):
			
		if (jour < 1 or jour > 31) or (mois < 1 or mois> 12) or annee < 0:
			print("cette année n'existe pas alorsne peut pas être créee")
		else:
			s.jour = jour
			s.mois = mois
			s.annee = annee

