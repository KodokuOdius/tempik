with open('output.txt', 'w') as _out:
    for i in range(int(input())):
        _in = open(input())
        _out.writelines(_in.read())
        _in.close()