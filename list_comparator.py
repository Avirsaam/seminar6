class ListsComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    @staticmethod
    def find_average(list):
        if len(list) == 0:
            raise ValueError
        else:
            sum = 0
            for i in list:
                sum += i
            return sum / len(list)

    def compare(self):
        try:
            if self.find_average(self.list1) == self.find_average(self.list2):
                return "Средние значения равны"
            elif self.find_average(self.list2) > self.find_average(self.list1):
                return "Второй список имеет большее среднее значение"
            return "Первый список имеет большее среднее значение"
        except ValueError:
            raise ValueError