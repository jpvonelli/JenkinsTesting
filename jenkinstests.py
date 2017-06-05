def func(f):
    if(f == 'Hello'):
        return "World"
    else:
        return 'Hello'


def test_answer():
    assert func('Hello') == 'World'
