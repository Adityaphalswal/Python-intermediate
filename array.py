#["January", "February","March","April","May"]
expense=[2200,2350,2600,2130,2190]
x=expense[1]-expense[0]
print(x)
total_expense=expense[0]+expense[1]+expense[2]
print(total_expense)
for i in range (len(expense)):
    if expense[i]== 2000:
        print(i)


expense.insert(5,1980)
new=expense[3]-200
print(new)
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
a=heros.append("Black Panther")

heros.pop()
print(heros)
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros.sort)

input=()
            


