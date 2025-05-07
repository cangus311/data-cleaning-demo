import unittest
import pandas as pd
from pipeline import clean_data

class TestPipeline(unittest.TestCase): # tells python this class contains tests
    def test_clean_data(self):   #starts with test_ so unittest knows it's a test
        df = pd.DataFrame({
            'name': [' Alice ', None, 'Bob'],
            'email': ['alice@email.com', 'bob@email.com', '']
        })  # this makes a pretend dataframe to test the function
        cleaned = clean_data(df)
        self.assertEqual(len(cleaned), 1)  #checks that dataframe has 1 row
        self.assertEqual(cleaned.iloc[0]['name'], 'Alice') #checks that name is 'Alice'

if __name__ == '__main__':
    unittest.main()
