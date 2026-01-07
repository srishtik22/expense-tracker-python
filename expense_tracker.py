exp={'coffee':20,"tea":15, "food":120,}
# print(exp)
def options():
  print('''
  menu options:
  1.add expense
  2.view expense
  3.show total
  4.exit
  ''')
choice=-1
while choice!=4:
    # print(options())- this was giving none in the output as options fuc already prints the menu
    options()
    choice=input("enter your choice:")
    if choice.isdigit():
        x=int(choice)
        if x==1:
          item=input("enter item name:")
          items=item.lower()
          amount=input(f"enter amount of the {item} :")
          if amount.isdigit():
             y=int(amount)
             exp[items]=exp[items]+y
          else:
              print("enter valid amount")

        elif x==2:
            if exp:
              for key in exp.keys():
                print(f"{key} = {exp[key]}")
            else:
                print("No expenses added yet.")

        elif x==3:
            # sum=0 instead of this use another name. it is already a built-in py func.
            if exp:
                tot=0
                for key in exp.keys():
                  tot=tot+exp[key]
                print(f"the total expense is: {tot}")
            else:
                print("No expenses added yet.")

        elif x==4:
            break

    else:
        print("invalid input. choose from menu")
