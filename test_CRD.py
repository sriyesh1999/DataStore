import unittest
from CRD import DataStore

class Test_Create(unittest.TestCase):
    def setUp(self) -> None:
        self.d=DataStore()
    def tearDown(self) -> None:
        self.d.delete("xyz")
    def test_create_Data(self):
        self.assertEqual(self.d.create("xyz",'{"abc":123}'),"Value Added")
    def test_read_data(self):
        self.d.create("xyz", '{"abc":123}')
        self.assertEqual(self.d.read("xyz"),{'abc':123})
    def test_delete_data(self):
        self.d.create("abc", '{"abc":123}')
        self.assertEqual(self.d.delete("abc"), "Deleted")
if __name__=='__main__':
    unittest.main()
