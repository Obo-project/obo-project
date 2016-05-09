from relations import hasPopulation
from relations import capital
from relations import diedin
from relations import diedondate
from relations import wasbornin
from relations import wasbornondate

listeRelation = [hasPopulation.hasPopulation, capital.capital, diedin.diedIn, diedondate.diedOnDate, wasbornin.bornIn, wasbornondate.bornOnDate]
grammar = hasPopulation.grammar
dic = hasPopulation.dic
