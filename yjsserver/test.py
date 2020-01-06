# 测试语句
# {"action":"connectDBAndQuery", "arg":"{\"type\":\"takeout\",\"detail\":\"overall\",\"district\":\"海淀\"}"}
# 构造数据包的语句
# {"data":"{\"yjsParams\":{\"package_name\":\"sys\",\"module_name\":\"sys\",\"module_class_name\":\"sys\"}}"}

import sys
import uuid
import copy

# a = [1, 2, [3, 4]]
# b = copy.copy(a)
# c = copy.deepcopy(a)
# d = a
#
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

print(uuid.NAMESPACE_DNS)