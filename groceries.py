print("---------------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------------")
import operator
products = sorted(products, key= operator.itemgetter("name"))
for product in products:
    price2 = ' (${0:.2f})'.format(product["price"])
    print("+ " + product["name"] + price2)
print("---------------")

print("---------------")
departments=[]
for product in products:
    departments.append(product['department'])
department_name=sorted(set(departments))
print("THERE ARE",len(department_name), "DEPARTMENTS:")
print("---------------")
mydept=[]
for dept_name in department_name:
    if departments.count(dept_name) == 1:
        mydept.append("+ " + dept_name.title()+" ("+str(departments.count(dept_name))+" product"+") ")
for dept_name in department_name:
    if departments.count(dept_name) != 1:
        mydept.append("+ " + dept_name.title()+" ("+str(departments.count(dept_name))+" products"+") ")
mydept.sort()
for d in mydept:
    print(d)
