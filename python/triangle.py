for i in range(1,10+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ( *(list(range(1,i + 1)) + list(range(i - 1, 0, -1))) )