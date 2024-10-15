import nanobind_example as m

def test_add():
    assert m.backend.add(1, 2) == 3
