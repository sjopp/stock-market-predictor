import unittest
from tests.context import src, return_dataframe_resource


class ScikitLearnTestCase(unittest.TestCase):

    def test_machine_learning_score(self):
        dataframe_values = return_dataframe_resource('MSFT/MSFT_2019.json', columns=['date', 'adjClose'])
        src.scikit_learn.convert_to_encoded(dataframe_values)


if __name__ == '__main__':
    unittest.main()
