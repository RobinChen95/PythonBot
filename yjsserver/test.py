# 测试语句
# {"action":"connectDBAndQuery", "arg":"{\"type\":\"takeout\",\"detail\":\"overall\",\"district\":\"海淀\"}"}
# 构造数据包的语句
# {"data":"{\"yjsJsonRpc\":\"0.1\",\"yjsMethod\":\"POST\",\"yjsParams\":{\"package_name\":\"sys\",\"module_name\":\"sys\",\"module_class_name\":\"__loader__\",\"params\":{\"arg1\":\"object_id\"}},\"yjsRequestId\":\"123456\" }"}

import sys

for x in sys.modules.keys():
    print(sys.modules[x])



