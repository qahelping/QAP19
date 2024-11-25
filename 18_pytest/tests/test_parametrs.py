from pytest import fixture, mark


def sum(a, b):
    if 0 <= a <= 100 and 0 <= b <= 100:
        return a + b
    else:
        return 'Error'


def delenie(a, b):
    if 0 < a <= 100 and 0 < b <= 100:
        return a / b
    else:
        return 'Error'


class TestParam:

    @mark.parametrize('a,b,result', [(1, 1, 2),
                                     (0, 0, 0),
                                     (100, 100, 200),
                                     (50, 50, 100),
                                     (-1, -1, 'Error'),
                                     (101, 101, 'Error')])
    def test_sum(self, a, b, result):
        assert sum(a, b) == result

    @mark.parametrize("a, b, expected", [
        (1, 1, 1),  # Граничное значение
        (100, 100, 1),  # Граничное значение
        (50, 2, 25),  # Среднее значение
        (0, 50, 'Error'),  # Недопустимое значение для a
        (50, 0, 'Error'),  # Недопустимое значение для b
        (101, 50, 'Error'),  # a больше 100
        (50, 101, 'Error'),  # b больше 100
        (100, 0, 'Error'),
        (1, 5, 0.2), (5, 1, 5), (100, 50, 2), (50, 100, 0.5), (99, 11, 9), (99, 99, 1), (0, 50, 'Error'),
        (50, 0, 'Error'), (101, 2, 'Error'), (30, 101, 'Error'), (-1, 5, 'Error'), (5, -1, 'Error')

    ])
    def test_del(self, a, b, expected):
        assert delenie(a, b) == expected

