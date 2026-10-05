Salaries = {"Asha":50000, "Babu":40000, "Siva":30000, "Mani":20000}

total= sum(Salaries.values())
count = len(Salaries)
Average = total / count
print("Average:", Average)

for name,salary in Salaries.items():
    if salary > Average:
        print(name,salary)

    
