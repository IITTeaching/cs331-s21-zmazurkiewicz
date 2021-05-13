import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    a = book_to_words()
    count = [0] * 128
    b = a
    mxchars = 0
    maxword = ""
    
    for x in a:#finding max
        if len(x) >= mxchars:
            maxword = x
            mxchars = len(x)
    
    for y in range(mxchars-1, -1, -1):
        try:
            t = x[y]
            count[x[y]] += 1
        except IndexError:
                count[0] += 1
        for y in range(1, (len(count)-1)):
            count[y] = count[y] + count[y-1]
        for y in range((len(a)-1), 0):
            index = count[a[x[y]]]
            b[index] = x[y]
            y -= 1
        for y in range(0, len(a)-1):
            a[y] = b[y]
            
    return a

a = book_to_words()
print(a)
a = radix_a_book()
print(a)