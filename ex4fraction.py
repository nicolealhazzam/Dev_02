def decompose(n): 
    res=[]
    i=2 
    while n>1: 
        while n%i==0: 
           res += [i]
           n=n/i 
        i=i+1 
    return res

class Fraction:
	def __init__(s,numerateur, denominateur):
		s.numerateur = numerateur
		s.denominateur = denominateur

	def __mul__(s, other):
		s.numerateur *= other.numerateur
		s.denominateur *= other.denominateur

	def __add__(s, other):
		if(other.denominateur == s.denominateur):
			s.numerateur += other.numerateur
		else:
			"""on rend les deux fractions au meme denominateur pour additioner"""
			a = s.denominateur
			s.numerateur *= other.denominateur

			s.denominateur *= other.denominateur
			other.numerateur *= a
			
			other.denominateur *= a		
			s.numerateur += other.numerateur

	def simplifie(s):
		a = decompose(s.numerateur)	
		b = decompose(s.denominateur)
		if a == b:
			s.numerateur = 1
			s.denominateur = 1
		else:
			for n in a:
				if n in b:
					a.remove(n)
					b.remove(n)
			s.denominateur = 1
			s.numerateur = 1
			for x in a:
				s.numerateur *= x
			for x in b:
				s.denominateur *= x


		print(s.numerateur)
		print (s.denominateur)
