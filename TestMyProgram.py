import unittest
import os

class TestMyProgram(unittest.TestCase):
    def test(self):
        print("Testing")
        os.system("C:\Users\Hazir\PycharmProjects\DA_project\Project.py")
        os.system("C:\Users\Hazir\PycharmProjects\DA_project\scrapy.py")




if __name__ == '__main__':
    unittest.main()