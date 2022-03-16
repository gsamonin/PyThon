import sys


def Vivod(*s, sep='', end='\n'):
    sys.stdout.write(str(s[0]))
    for i in range(1, len(s)):
        if sep == '':
            sys.stdout.write(' ')
        else:
            sys.stdout.write(sep)
        sys.stdout.write(str(s[i]))
    sys.stdout.write(end)


if __name__ == '__main__':
    Vivod({'jora': 123}, end='\n'+'-'*10)
