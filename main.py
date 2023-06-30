from pyswip import Prolog

prolog = Prolog()


prolog.consult(r"knowledgebase.pl")
print(list(prolog.query("finalPredicate")))
