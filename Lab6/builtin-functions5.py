def all_true(tuple):
    return all(tuple)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
print(all_true(tuple1))
print(all_true(tuple2))