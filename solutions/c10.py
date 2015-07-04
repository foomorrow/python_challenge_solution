'''
a = [1, 11, 21, 1211, 111221,
'''

def gen_a(ind):
    return ind == 0 and '1' or ''.join(map(lambda x:str(x[0])+x[1], reduce(lambda x,acc: len(x) > 0 and acc == x[-1][1] and (x[0:-1] + [(x[-1][0]+1,acc)]) or (x + [(1,acc)]),gen_a(ind - 1),[])))



answer = str(len(gen_a(30)))
