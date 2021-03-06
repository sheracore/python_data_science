# python_pure_concepts

### Different between append and extend in list is that by extend you can add multiple items but by append you can add just one
```
list = [1,2,3]
list.append([2,5])
  res = [1,2,3,[2,5]]
list.extend([2,5])
  res = [1,2,3,2,5]
```

### list methods
```
list = [1,2,3]
del(a[0])
```

## Immutable and mutable
### list is mutable and tuple is immutable the following id is id refrenced in ram
```
 list = [1,2,3]
 id(list)
140674943444104
 list.append(4)
 id(list)
140674943444104 
 tuple = (1,3,4)
 id(tuple)
140674943235848
 tuple = tuple + (2,)
 id(tuple)
140674943825304
```
It means you can do these:
```
 list = [1,3,4]
 list2 = list
 list.extend([5,6,7])
 list
[1, 3, 4, 5, 6, 7]
 list2
[1, 3, 4, 5, 6, 7] 

 list = [1,3,4]
 list2 = list[:]
 list2
[1, 3, 4]
 list.append(45)
 list2
[1, 3, 4] 
```

# Sets
Sets are a type of collection. This means that like lists and tuples, you
can input different python types. 
Unlike lists and tuples they are unordered.This means sets do not record element position. 
Sets only have unique elements. This means there is only one of a particular element in a set.
```
 set1 = {"a", "a", "b", "c"}
 set1
{'a', 'c', 'b'}
 set1 = {"a":"12", "a" : "45", "b": "56", "c": "98"}
 set1
{'a': '45', 'b': '56', 'c': '98'}
 set1 = {"a":"12", "a" : "45", "b": "56", "c": "98"}
 set1
{'a': '45', 'b': '56', 'c': '98'}

 list = [1,2,4,"tiger","tiger", "tylor"]
 set(list)
{1, 2, 4, 'tylor', 'tiger'}
 
 
 set2 = {"a","b","c","d","e"}
 set2.add("f")
 set2
{'f', 'e', 'b', 'a', 'd', 'c'}
 set2.add("f")
 set2
{'f', 'e', 'b', 'a', 'd', 'c'}
 set2.remove("f")
 {'e', 'b', 'a', 'd', 'c'}
 
'a' in set2
True


----- & ----

 set1 = {"a","b","c","d","e"}
 set2 = {"a", "b", "name"}
 set3 = set1 & set2
 set3
{'a', 'b'}

----- union ----
set1.union(set2)
{'d', 'c', 'e', 'b', 'a', 'name'}

---- issubset ----
 set1 = {1,2,3}
 set2 = {1,2,3,4}
 set1.issubset(set1)

set1.symmetric_difference(set2)
{4}

```
# Dictionaries
The keys have to be immutable and unique
The values can be immutable, mutable and and duplicates
```
dict = {"a" : "b", "1" : 2}
 dict
{'a': 'b', '1': 2}
 dict["1"]
2
 dict["a"]
 dict["a"] = "new_value"
 del(dict["a"])
 
 "a" in dict
 False
 
 dict.keys()
 dict.values()
 
 dict.get("a")
 res --> "b"
 
 dict.get("c", None)
 res --> None
 
 dict.get("c", "X")
 res --> "X"
 
```

# Functions
```
def ArtistNames(*names):
    print(names)
    
ArtistNames("Hassan", "Ali", "Mohsen")
```
### Global Scope
```
x is global variable
ArtistNames(x):
    return x + " ghaffari"

x="mohamad"
ArtistNames(x):
print(x):
    "mohamad ghaffari"
```
### Set variable global in function
```
def pinkfloyd():
    global ClaimedSales
    ClaimedSales = "45 million"
    return ClaimedSales

pinkfloyd()
print(ClaimedSales)
"45 million"
```

# Objects and Classes
### Function init is a constructor
```
class Circle(object):

    def __init__(self, radius, color):
      # Attributes
      self.radius = radius
      self.color = color


class Rectangle(object):

    def __init__(self, height, width, color):
      # Attributes
      self.height = height
      self.width = width
      self.color = color
   
Now we can have several ojects of any class

C1 = Circle(10, "red")
C2 = Circle(0.001, "Pink")
C1.color = "Blue"
C2.radius = 1


Class methods:

class Circle(object):

    def __init__(self, radius, color):
        # Attributes
        self.radius = radius
        self.color = color
      
    def add_radius(self,r):
        self.radius = self.radius + r

Default value in constructor:
def __init__(self, radius=10, color='red'):

dir(NmaeOfObject)
dir() method is useful for obtaining the list of data attributes and methods associated
dir(Circle)
```

# Reading file with open
```
file1 = open("/resources/data/example.txt", "w")
file1.close

with open(""/resources/data/example.txt"", "w") as f:
    file_read = f.read()

print(f.closed()) ---> True
print(file_read) ---> You can't access to file_read out of with indention

with open is better practice because it automaticlly closes the file
```









