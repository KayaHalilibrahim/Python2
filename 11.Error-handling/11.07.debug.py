import pdb

# used to follow the code step by step.

one = "one"
two = "two"

pdb.set_trace()  # It stops here.

result = one + two

three = "three"

result += three

print(result)

# pdb komutları:
# l --> (list): Kodun etrafındaki satırları listeler.
# n --> (next): Bir sonraki satıra geçer.
# p --> (print): Bir değişkenin mevcut değerini gösterir. Örn: p one
# c --> (continue): Programın çalışmasına normal şekilde devam eder.

"""
Output:
-> result = one + two
(Pdb) l
  3     one = "one"
  4     two = "two"
  5  
  6     pdb.set_trace()  # It stops here.
  7  
  8  -> result = one + two
  9  
 10     three = "three"
 11  
 12     result += three
 13  
(Pdb) p one
'one'
(Pdb) p two
'two'
(Pdb) p three
*** NameError: name 'three' is not defined
(Pdb) n
> /media/halilibrahim/Yeni Birim/pythonProjects/11.Error-handling/11.07.debug.py(10)<module>()
-> three = "three"
(Pdb) p three
*** NameError: name 'three' is not defined
(Pdb) n
> /media/halilibrahim/Yeni Birim/pythonProjects/11.Error-handling/11.07.debug.py(12)<module>()
-> result += three
(Pdb) p three
'three'
(Pdb) n 
> /media/halilibrahim/Yeni Birim/pythonProjects/11.Error-handling/11.07.debug.py(14)<module>()
-> print(result)
(Pdb) p result
'onetwothree'
(Pdb) c
onetwothree
"""