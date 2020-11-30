def canPlaceFlowers(flowerbed, n):
    """
    We can put flower in every three contiguous empty spots,
    after put that flower in the middle of three,
    the third one can be counted into the "next three spots".
    So we set the count variable to be 1.
    """
    
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    print(flowerbed)

    count = 0

    for f in flowerbed:
        if f == 0:
            count += 1
        else:
            count = 0

        if count == 3:
            n -= 1
            count = 1

        if n == 0:
            return True
    return False


a = list(map(int, input().split()))
print(canPlaceFlowers(a, int(input())))
