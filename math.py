__author__ = 'Tracy'

def add(x,y):
    return x + y
	
def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

if '__main__' == __name__:
    print("3 + 4 should give....%d" % add(3,4))
    print("9 - 4 should give....%d" % sub(9,4))
    print("9 * 4 should give....%d" % mult(9,4))
