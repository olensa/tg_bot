from pathlib import Path
from csv import reader

new_list = []
my_file = Path("name.csv")
def ckeckList(lst):
  
    ele = lst[0]
    chk = True
      
    # Comparing each element with first item 
    for item in lst:
        if ele != item:
            chk = False
            break
    if (chk == True): 
        return True
    
if my_file.is_file():

    with open('name.csv', 'r') as f:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(f)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
                id = row[3]
                if str(83017015)==id:
                    name = row[1]
                    last_name = row[2]
                    age = row[0]
        print(name)
        print(age)
        print (last_name)    
        print (id)

a = 88
b = '88'
print (str(a)==b)

        
