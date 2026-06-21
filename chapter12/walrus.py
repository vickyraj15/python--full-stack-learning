# Using walrus operator
if( n :=len([1,2,3,4,5])) >3:
    print(f"list is too long({n} element, expected  < = 3)")

#output: List is too long( 5elements, expected <= 3)
