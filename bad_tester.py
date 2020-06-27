from nearest import nearest_square

# unit test sampling
print("Nearest square <= 5:", nearest_square(5))
print("Nearest square <= 12:", nearest_square(-12))
print("Nearest square <= 9:", nearest_square(9))
print("Nearest square <= 23:", nearest_square(23))

# expected results annotated
print("Nearest square <= 5: returned {}, expected answer: 4".format(nearest_square(5)))
print("Nearest square <= 12: returned {}, expected answer: 0".format(nearest_square(-12)))
print("Nearest square <= 9: returned {}, expected answer: 9".format(nearest_square(9)))
print("Nearest square <= 23: returned {}, expected answer: 16".format(nearest_square(23)))

# improved for a large unit testing
nearest_5 = nearest_square(5)
print("Nearest square <= 5: returned {}, expected answer: 4".format(nearest_5))
assert(nearest_5 == 4)

nearest_n12 = nearest_square(-12)
print("Nearest square <= 12: returned {}, expected answer: 0".format(nearest_n12))
assert(nearest_n12 == 0)

nearest_9 = nearest_square(9)
print("Nearest square <= 9: returned {}, expected answer: 9".format(nearest_9))
assert(nearest_9 == 0) # stop the programme in the case of error

nearest_23 = nearest_square(23)
print("Nearest square <= 23: returned {}, expected answer: 16".format(nearest_23))
assert(nearest_23 == 16)
