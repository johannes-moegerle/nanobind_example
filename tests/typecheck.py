import nanobind_example as m
m.backend.add(1, 2)
m.backend.add(1, "a")

from nanobind_example import backend
backend.add(1, 2)
backend.add(1, "a")

from nanobind_example.backend import add
add(1, 2)
add(1, "a")
