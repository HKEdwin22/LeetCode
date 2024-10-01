def test(flowerbed: list[int], n: int) -> bool:
    length = len(flowerbed)
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, length + 1):
        if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
    return n <= 0

if __name__ == '__main__':
#    flowerbed = [0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]
    # flowerbed = [0,1,0,1,0,1,0,0]
    # flowerbed = [0,0] 
    flowerbed = [1,0,0,0,0,0,1]
    n = 2 
    test(flowerbed, n)
