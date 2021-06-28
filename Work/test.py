import csv

data = []
with open("d:/ProjetDev/python/python-master/Work/Data/portfoliodate.csv") as source:
    reader = csv.reader(source)
    headers = next(reader)
    select = ["name", "shares", "price"]
    indices = [headers.index(n) for n in select]

    for line in reader:
        data.append({colname: line[index] for colname, index in zip(select, indices)})
    print(data)