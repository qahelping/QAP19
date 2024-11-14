from pytest import fixture


@fixture(autouse=True)
def condition():
    print("\n===================")
    print("fixture precondition")
    print("===================")

    yield 42

    print("\n*******************")
    print("fixture postcondition")
    print("**********************")


@fixture()
def get_number():
    return 42