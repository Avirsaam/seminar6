from unittest import TestCase
from list_comparator import ListsComparator

test_list1 = [5]
test_list2 = [5,10]
test_list3 = [5,10,15]
test_average3 = 10

class ListsComparatorTests(TestCase):
    def setUp(self):
        self.comparator = ListsComparator(test_list3, test_list2)

    def test_find_average(self):
        self.assertEqual(test_average3, self.comparator.find_average(test_list3), "вычисление среднего значения списка неверно")

    def test_greater(self):
        self.assertEqual('Первый список имеет большее среднее значение', self.comparator.compare(),
                         "ошибка сравнения если первый список больше")

    def test_less(self):
        self.comparator.list1 = test_list1
        self.assertEqual("Второй список имеет большее среднее значение", self.comparator.compare(),
                         "ошибка сравнения если второй список больше")

    def test_equal(self):
        self.comparator.list2 = test_list3
        self.assertEqual("Средние значения равны", self.comparator.compare(),
                         "ошибка когда списки равны")

    def test_exception_rose(self):
        self.comparator.list1 = []
        with self.assertRaises(ValueError, msg="ошибка не генерируется"):
            self.comparator.compare()


