
from list_comparator import ListsComparator as Comparator

if __name__ == '__main__':
    list_odd = [1,3,5,7,9]
    list_even = [2,4,6,8,10]

    result = Comparator(list_odd, list_even).compare()
    print(result)

