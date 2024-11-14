from pytest import mark, fail


class TestMain:

    @mark.blocker
    def test_main(self):
        assert 'stackoverflow' in 'ru.stackoverflow.com'

    @mark.blocker
    @mark.skip
    def test_plus(self):
        assert 123 + 14 == 137

    @mark.critical
    @mark.xfail
    def test_minus(self, condition):
        assert 123 - 14 == condition, f'Error in, expected 123-14 = {123 - 14}, but actual {condition}'
        fail("error message")

    @mark.xfail
    def test_boolean_false(self):
        assert False

    @mark.xfail
    def test_boolean_true(self):
        assert True

    def test_boolean(self):
        assert bool('stackoverflow') == True

    def test_str(self):
        value = 'stackoverflow'
        assert len(value) == 12
