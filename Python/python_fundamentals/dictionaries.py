# # function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


def dictInTupleOut(xyz):
    dict_list = xyz.items()
    return dict_list  


# print (dictInTupleOut(my_dict))

def zipDict(list1, list2):
  newDict = dict(zip(list1, list2))
  return newDict


keys = ['a', 'b', 'c']
values = [1, 2, 3]

print (zipDict(keys, values))