y=int(input("Enter a year: "))

def out(y):
    year=["hou","ji","gou","zhu","shu","niu","hu","tu","long","she","ma","yang"]
    print(year[y%12])

out(y)