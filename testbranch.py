import unittest

def testSandwich(sandwich):
    firstItem = [sandwich[0]]
    lastItem = [sandwich[-1]]
    if firstItem == lastItem:
        print("it's a sandwich")
        return True
    else:
        return False

def testSoup(soup):
    for item in soup:
        if item == 'broth' or 'liquid':
            print("it's a soup")
            return True



