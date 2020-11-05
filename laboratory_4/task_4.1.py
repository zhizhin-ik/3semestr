import sys

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Слишком мало параметров')
        sys.exit(1)
    if len(sys.argv)>3:
        print('Слишком много параметров')
        sys.exit(1)
    if sys.argv[1]=='-n':
        param_value = int(sys.argv[2])
    else:
        param_value = int(sys.argv[1])
    if param_value==1 or param_value==2:
        print('1')
    else:
        a=[1,1]+[0]*(param_value-2)
        for i in range(2,param_value):
            a[i]=a[i-2]+a[i-1]
        print(a[param_value-1])