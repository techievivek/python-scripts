from tabulate import tabulate as table
data=[["Vivek",23,"NIT Agartala"],["Vikas",24,"AIIMS-Delhi"],["Rahul",22,"Patna Science College"]]
headers=["Name","Age","College"]
print(table(data,headers=headers))

#The above code is most basic table form.
#Let's play with it.
#Take data as dictionary.
data={"Name":["Vivek",23,"NIT Agartala"],"Age":["Vikas",24,"AIIMS-Delhi"],"College":["Rahul",22,"Patna Science College"]}
#Each key will be working as a header for our table.
#Each data for each key will be a row in our table.
print(table(data))
#Add headers
print(table(data,headers="keys"))
print()
#Lets style our table differently.
# plain, simple, grid, html, github, pretty, fancy_grid
print(table(data,headers="keys",tablefmt="plain"))
print(table(data,headers="keys",tablefmt="simple"))
print(table(data,headers="keys",tablefmt="grid"))
print(table(data,headers="keys",tablefmt="fancy_grid"))
print(table(data,headers="keys",tablefmt="github"))
print(table(data,headers="keys",tablefmt="pretty"))
print(table(data,headers="keys",tablefmt="html"))
#We can also given numbering to each row-data
print(table(data,headers="keys",tablefmt="grid",showindex="always"))
