from pytest import fixture, mark


@fixture()
def precondition():
    print("\n===================")
    print("usefixtures precondition")

    print("===================")


@mark.usefixtures("precondition")
def test_main():
    print('\n=======test main======')
    assert 'stackoverflow' in 'ru.stackoverflow.com'


class TestMain():

    def test_main(self):
        print('\n=======test 1======')
        assert 'stackoverflow' in 'ru.stackoverflow.com'

    def test_main2(self):
        print('\n=======test 2======')
        assert 'stackoverflow' in 'ru.stackoverflow.com'
