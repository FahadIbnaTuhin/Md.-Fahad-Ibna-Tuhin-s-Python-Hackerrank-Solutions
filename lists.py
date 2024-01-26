a = []
for _ in range(int(input())):
    command, *line = input().split()
    if command == "print":
        print(a)
    elif command == "insert":
        a.insert(int(line[0]), int(line[1]))
    elif command == "remove":
        a.remove(int(line[0]))
    elif command == "append":
        a.append(int(line[0]))
    elif command == "sort":
        a.sort()
    elif command == "pop":
        a.pop()
    else:
        a.reverse()
