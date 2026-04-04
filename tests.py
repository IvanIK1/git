import sys
import os

# Добавляем папку my_project в пути поиска
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Теперь можно импортировать из sort_algs.py
from sort_algs import quick_sort, merge_sort 


def test_q_sort_normal():
    assert quick_sort(arr = [2,3,1,2]) == [1 , 2 , 2 , 3] , f"Ошибка!!: {quick_sort()}"

def test_q_sort_empty():
    assert quick_sort(arr = []) == [], f"Ошибка!!: {quick_sort()}"
def test_q_sort_single():
    assert quick_sort(arr = [ 42]) == [42], f"Ошибка!!: {quick_sort()}"
def test_m_sort_normal():
    assert merge_sort(arr = [2,3,1,2]) == [1 , 2 , 2 , 3], f"Ошибка!!: {merge_sort()}"
def test_m_sort_empty():
    assert merge_sort(arr = []) == [], f"Ошибка!!: {merge_sort()}"
def test_m_sort_single():
    assert merge_sort(arr = [ 42]) == [42], f"Ошибка!!: {merge_sort()}" 

if __name__ == "__main__":
    test_q_sort_normal()
    test_q_sort_empty()
    test_q_sort_single()
    test_m_sort_normal()
    test_m_sort_empty()
    test_m_sort_single()
    print("Все тесты пройденны!")

