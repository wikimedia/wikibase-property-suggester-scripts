from testtools import TestCase
from testtools.matchers import *

from propertysuggester.evaluator import SearchResultEvaluation

class WikiDataApiTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    def test_evaluator(self):
        eval =SearchResultEvaluation()
        eval.evaluate()
        self.assertThat(1, Equals(1))
