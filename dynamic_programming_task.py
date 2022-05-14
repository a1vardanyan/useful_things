#Let's play a game: 
#There are n white balls and m black balls in a black box. If you get a white ball out your payoff +1, and -1 with a black ball. You can stop anytime and repeat the game infinite times. Will you play the game?

def mycache(foo):   # декоратор
    a = dict()
    def wrapper(n, m):
        if "{}{}".format(n,m) in a:
            return a["{}{}".format(n,m)]
        a["{}{}".format(n,m)] = foo(n, m)
        return a["{}{}".format(n,m)]
    return wrapper


@mycache
def E(n,m):
    #n - num of white balls
    #m - num of black balls
    if n == m == 0:
        return 0
    if m == 0:
        return n
    elif n == 0:
        return 0
    else:
        return max(0,n/(n+m) * (1+E(n-1,m))+m/(n+m) * (E(n,m-1)-1))
