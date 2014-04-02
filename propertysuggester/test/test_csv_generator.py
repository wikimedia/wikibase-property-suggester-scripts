from StringIO import StringIO
import unittest
from testtools import TestCase
from testtools.matchers import Equals
from propertysuggester import CsvGenerator


class CsvGeneratorTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.file = StringIO()

    def testCreateTable(self):
        table = {(1, None): {'appearances': 8, 2: 5, 3: 0}}
        CsvGenerator.create_pair_csv(table, self.file)

        self.file.seek(0)
        self.assertThat(self.file.readline().strip(), Equals("pid1;qid1;pid2;count;probability"))
        prob = 5.0 / 8.0
        self.assertThat(self.file.readline().strip(), Equals("1;null;2;5;{0}".format(prob)))

        print self.file.read()



if __name__ == '__main__':
    unittest.main()