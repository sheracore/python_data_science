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
>>> set1 = {"a", "a", "b", "c"}
>>> set1
{'a', 'c', 'b'}
>>> set1 = {"a":"12", "a" : "45", "b": "56", "c": "98"}
>>> set1
{'a': '45', 'b': '56', 'c': '98'}
>>> set1 = {"a":"12", "a" : "45", "b": "56", "c": "98"}
>>> set1
{'a': '45', 'b': '56', 'c': '98'}

```








