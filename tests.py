import unittest
from tada_hdt_entity.entity import EntityAnn
from tada_hdt_entity.parser import Parser

# import entity
# from entity import EntityAnn
# from parser import Parser

hdt_file = "test.hdt"
log_file = "tests.log"


class TestAll(unittest.TestCase):
    def test_subject_column(self):
        """
        Equivalent to
            TEST(EntityTest, nonSubjectColumnsHeuristic)
        :return:
        """
        dbp_country = "http://dbpedia.org/property/country"
        class_uri = "http://dbpedia.org/ontology/Wrestler"
        p = Parser("test_files/test8.csv")
        data = p.parse_vertical()
        ea = EntityAnn("test.hdt","tests.log", 0.9)
        ea.set_alpha(0.9)
        ea.set_title_case(False)
        properties = ea.annotate_entity_property_column(data, 1, 2)
        # print("properties")
        # print(properties)
        # properties = entity.deref_list_string(properties)
        # for p in properties:
        #     print(p)
        # print("p size: ")
        # print(properties.size())
        # p_vals = entity.std_list.get_value(properties)
        self.assertEqual(0, properties.size())
        properties = ea.annotate_entity_property_heuristic(data, class_uri, 2)
        # print("2nd properties")
        # print(properties)
        # print("first item: ")
        # print(properties[0])
        self.assertEqual(properties[0], dbp_country)


if __name__ == '__main__':
    unittest.main()