import unittest
from tool import infer, validate

class SchemaTests(unittest.TestCase):
    def test_infer_and_validate(self):
        rows = [{"id":"1", "score":"2.5", "name":"a"}, {"id":"2", "score":"", "name":"b"}]
        self.assertEqual(infer(rows), {"id":"int", "score":"float", "name":"str"})
        self.assertEqual(validate(rows, {"id":"int", "score":"float"}), [])
        self.assertEqual(len(validate(rows, {"id":"bool"})), 2)

if __name__ == "__main__": unittest.main()
