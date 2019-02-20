from sys import stdin,stdout

def main():
    n=stdin.readline()

    arr=[int(x) for x in stdin.readline().split()]

    sum=0
    for x in arr:
        sum+=x
    stdout.write(str(sum))

if __name__=="__main__":
    main()