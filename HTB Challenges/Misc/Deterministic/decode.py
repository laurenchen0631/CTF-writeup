from curses.ascii import isdigit


linked = {}
head = set[int]()
tail = set[int]()

with open('deterministic.txt', 'r') as f:
    f.readline()
    f.readline()
    for line in f:
        [parent, val, child] = line.rstrip().split(' ')
        head.add(int(parent))
        tail.add(int(child))
        linked[int(parent)] = (int(val) if val.isdigit() else ord(val), int(child))

print(head - tail)
print(tail - head)

for i in range(1, 255):
    cur = (head - tail - {100}).pop()
    end = (tail - head).pop()
    nextchild = linked[cur][1]
    print(i)
    while nextchild != end:
        print(chr(linked[cur][0] ^ i), end='')
        cur = nextchild
        nextchild = linked[cur][1]
    print()

