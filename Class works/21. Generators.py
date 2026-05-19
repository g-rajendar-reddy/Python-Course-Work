
def reels():
    data = ['1..100','101..200','201..300','301..400']
    for i in data:
        yield i

scroll = reels()
print(next(scroll))
print(next(scroll))


def display():
    for i in range(1, 11):
        yield i

num = display()   # create generator object
print(num)

for value in num:
    print(value)


def reels():
    yield "1st set"
    yield "2nd set"
    yield "3rd set"

scroll = reels()
print(next(scroll)) 
print(next(scroll))
print(next(scroll))

# Output: 1st set
#         2nd set
#         3rd set



def music(tracks):
    for track in tracks:
        yield track

playlist = music(['song1', 'song2', 'song3'])
print(next(playlist))
print(next(playlist))