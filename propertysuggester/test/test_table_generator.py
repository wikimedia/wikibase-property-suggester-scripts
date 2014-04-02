import unittest
from testtools import TestCase
from testtools.matchers import *
from propertysuggester import MatrixGenerator
from propertysuggester.utils.datatypes import Entity, Claim

test_data1 = [Entity('Q15', [Claim(31, 'wikibase-entityid', 'Q5107'),
                             Claim(373, 'string', 'Africa')]),
              Entity('Q16', [Claim(31, 'wikibase-entityid', 'Q384')])]

test_data2 = [Entity('Q15', [Claim(31, 'wikibase-entityid', 'Q12'),
                             Claim(31, 'wikibase-entityid', 'Q5107'),
                             Claim(373, 'string', 'Africa'),
                             Claim(373, 'string', 'Europe')])]



class TableGeneratorTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)

    def testTableGenerator(self):
        table = MatrixGenerator.compute_table(test_data1, [])
        self.assertThat(table, ContainsAll(((31, None), (373, None))))
        self.assertThat(len(table), Equals(2))

        self.assertThat(table[(31, None)]['appearances'], Equals(2))
        self.assertThat(table[(31, None)][31], Equals(0))
        self.assertThat(table[(31, None)][373], Equals(1))

        self.assertThat(table[(373, None)]['appearances'], Equals(1))
        self.assertThat(table[(373, None)][373], Equals(0))
        self.assertThat(table[(373, None)][31], Equals(1))

    def testTableWithMultipleOccurance(self):
        table = MatrixGenerator.compute_table(test_data2, [])
        self.assertThat(table, ContainsAll(((31, None), (373, None))))
        self.assertThat(len(table), Equals(2))

        self.assertThat(table[(31, None)]['appearances'], Equals(1))
        self.assertThat(table[(31, None)][31], Equals(0))
        self.assertThat(table[(31, None)][373], Equals(1))

        self.assertThat(table[(373, None)]['appearances'], Equals(1))
        self.assertThat(table[(373, None)][373], Equals(0))
        self.assertThat(table[(373, None)][31], Equals(1))

    def testTableWithClassifier(self):
        table = MatrixGenerator.compute_table(test_data2, [31])
        self.assertThat(table, ContainsAll(((31, 12), (31, 5107), (373, None))))
        self.assertThat(len(table), Equals(3))

        self.assertThat(table[(31, 12)]['appearances'], Equals(1))
        self.assertThat(table[(31, 12)][31], Equals(0))
        self.assertThat(table[(31, 12)][373], Equals(1))

        self.assertThat(table[(31, 5107)]['appearances'], Equals(1))
        self.assertThat(table[(31, 5107)][31], Equals(0))
        self.assertThat(table[(31, 5107)][373], Equals(1))

        self.assertThat(table[(373, None)]['appearances'], Equals(1))
        self.assertThat(table[(373, None)][373], Equals(0))
        self.assertThat(table[(373, None)][31], Equals(1))


if __name__ == '__main__':
    unittest.main()