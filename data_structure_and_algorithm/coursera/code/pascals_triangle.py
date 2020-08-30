#파스칼 삼각형의 n번째 층의 값들을 찾아라

def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    
    triangle = [[0]*(n+1) for i in range(n+1)]

    triangle[0][0] = 1
    for i in range(1,n+1) :
        for j in range(i) :
            if j  ==  0 or triangle[i-1][j] == 0 :
                triangle[i][j] = 1
            else :
                triangle[i][j] = triangle[i-1][j-1] +triangle[i-1][j]
    return triangle,triangle[n]