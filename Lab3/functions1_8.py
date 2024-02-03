def spy_game(nums):
    list = [0, 0, 7, 'x']
    for x in nums:
        if x == list[0]:
            list.pop(0)
    return len(list) == 1