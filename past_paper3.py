def average_age(people):
    """
    param people: list of tuples (name, age)
    returns     : return average age of people
    """
    return sum(p[1] for p in people) / len(people)

def rectangle(p1, p2):
    """
    param p1: tuple of points
    param p2: tuple of points 
    returns : dictionary with keys area, sc, y
    """
    dx = (p2[0] - p1[0])
    dy = (p2[1] - p1[1])
    area = dx*dy
    xc = p1[0] + dx/2
    yc = p1[1] + dy/2
    return {'area':area, 'xc':xc, 'yc':yc}

def word_count(s):
    """
    param s: words
    returns: number of words in string
    """
    return len(s.split(" "))


def long_word(s):
    """
    param s: sentence
    returns: longest word in list
    """
    wordsAsList = s.split(' ')
    longestWord = wordsAsList[0]    
    for word in s.split(' '):
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord

def shift(a):
    """
    param a: list
    returns: list contsains same elements as a
             but positions have been shifted by 1
    1
    a = 0 1 2 3 
    b = 1 2 3  
    """
    b = []
    currentPos = 0
    for i in range(len(a)-1):
        if currentPos > a.index(a[-1]):
            currentPos = 0
        else:
            currentPos += 1
        b.append(a[currentPos])        
    return b
    
    

    
