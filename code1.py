# creating a function and assigning parameters
def linearsearchproduct(productlist, targetproduct):
   indices=[]
   for index, product in enumerate(productlist):
    if product == targetproduct:
        indices.append(index)
   return indices
products=["pencil","scale","pencil","pen",
"pencil"]
target="pencil"
result=linearsearchproduct(products,target)
print(result)