from tada_hdt_entity.entity import EntityAnn
from tada_hdt_entity.parser import Parser
dbp_country = "http://dbpedia.org/property/country"
class_uri = "http://dbpedia.org/ontology/Wrestler"
p = Parser("../test_files/test8.csv")
data = p.parse_vertical()
ea = EntityAnn("../test.hdt","../tests.log", 0.9)
ea.set_alpha(0.9)
ea.set_title_case(False)
properties = ea.annotate_entity_property_column(data, 1, 2)
