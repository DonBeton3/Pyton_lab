
from sys import path
path.append('./modules')  

import module  

result_add = module.add(10, 20)
result_multiply = module.multiply(10, 20)

print(f"10 + 20 = {result_add}")
print(f"10 * 20 = {result_multiply}")