import itertools
geek=["sun","flower","peoples","Animals","Day","night"]
partition=list(zip(*[iter(geek)] * 2))
print(partition)

print(" taking the string as input and convert it into list")

formatted_list=list(map(int,input().split()))
print(formatted_list)

x=[[1,2],[3,4],[5,6]]

list=list(itertools.chain.from_iterable(x))
print(list)