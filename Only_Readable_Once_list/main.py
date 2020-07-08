from Only_Readable_Once_list.SecureList import *

messages = SecureList([1, 2, 3, 4])
messages1 = [1, 2, 3, 4]
print(messages[1])  # prints 2
print(messages)     # prints [1,3,4]
