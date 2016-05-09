from relations import hasPopulation
from relations import capital
from relations import diedin
from relations import diedondate
from relations import wasbornin
from relations import wasbornondate
from relations import hasgdp
from relations import hasPopulationDensity

listeRelation = [hasPopulation.hasPopulation, capital.capital, diedin.diedIn, diedondate.diedOnDate, wasbornin.bornIn, wasbornondate.bornOnDate, hasgdp.hasGDP, hasPopulationDensity.hasPopulationDensity]
grammar = hasPopulationDensity.grammar + hasPopulation.grammar
dic = hasPopulation.dic
dic.update(hasPopulationDensity.dic)
