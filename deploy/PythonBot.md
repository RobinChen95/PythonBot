# PythonBot
## 基本约束
1.	python version 3.5 及以上

## 互操作约定
### Java 调用 json 接口规范


#### 目前要解决的问题:

## 解决方法：


## API
### api 公共说明
~~~
request:
{
    "yjsJsonRpc": "0.1", 			// json rpc version（暂时没用上）
    "yjsMethod": "POST", 			// http request method
    "yjsParams": {		  			// request argument body
        "package_name": "",
        "module_name": "",
        "module_func_name": "",
        "params": {
            "arg1": "object_id1",
            "arg2": "object_id2"
        }
    },
    "yjsRequestId": "123456"		// request response id（暂时没用上）
}
result: 
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {					// http response result body
        "res": {}
    },
    # "yjsError": {},				// http response error body(optional)
    "yjsResponseId": "123456"			
}
yjsError:								// http response error body(optional)
{	
    "code": "30500",						// error code
    "message": "package not found", 			// error shortcut message
    "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}				// error detail
}
~~~
### /api/availablePackages
####请求说明
* 请求方法 GET
* 请求参数格式 无

####接口描述
获取可以使用的package，不包含Python 内置package
#### 参数说明
无
####postman 请求参数示例
~~~
无
~~~

####返回说明
~~~
{
    "yjsResponseId": "123456",
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "availablePackages": {
            "packages": [
                "sample",
                "yjsexample"
            ]
        }
    }
}
~~~


### /api/availableModules
####请求说明
* 请求方法 GET
* 请求参数格式 无

####接口描述
获取可以使用的module，不包含Python 内置module
#### 参数说明
无

####postman 请求参数示例
~~~
无
~~~

####返回说明
~~~
{
    "yjsResponseId": "123456",
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "availableModules": {
            "modules": [
                "sample",
                "yjsexample",
                "yjsexample.sample"
            ]
        }
    }
}
~~~

### /api/packageAllInfo/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
获取给定包名的相关信息，只有module信息
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
package_name  | string  | 是  | Python package name

####postman 请求参数示例
~~~
{
    "yjsJsonRpc": "0.1", 			
    "yjsMethod": "POST", 		
    "yjsParams": {		  		
        "package_name": "yjsexample"
    },
    "yjsRequestId": "123456"	
}
~~~

####返回说明
~~~
{
    "yjsResponseId": "123456",
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "packageTotalInfo": {
            "module_names": [
                "yjsexample.sample"
            ],
            "package_name": "yjsexample"
        }
    }
}
~~~


### /api/moduleInfo/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
获取给定模块名的相关信息，包含模块的函数信息和类信息
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
module_name  | string  | 是  | Python module name

####postman 请求参数示例
~~~
{
    "yjsJsonRpc": "0.1", 			
    "yjsMethod": "POST", 		
    "yjsParams": {		  		
        "module_name": "yjsexample.sample"
    },
    "yjsRequestId": "123456"	
}
~~~

####返回说明
~~~
{
    "yjsResponseId": "123456",
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "moduleInfo": {
            "module_func": [
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                },
                {
                    "func_name": "moduleFunc1",
                    "func_sig": "(arg_a)"
                }
            ],
            "classes": [
                {
                    "class_func": [
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        }
                    ],
                    "class_method": [
                        {
                            "method_sig": "()",
                            "method_name": "classMethod"
                        }
                    ],
                    "class_name": "A",
                    "class_sig": {
                        "init_sig": "(self, age)"
                    }
                },
                {
                    "class_func": [
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        },
                        {
                            "func_name": "sayHello",
                            "func_sig": "(self, name)"
                        }
                    ],
                    "class_method": [
                        {
                            "method_sig": "()",
                            "method_name": "classMethod"
                        }
                    ],
                    "class_name": "B",
                    "class_sig": {}
                }
            ],
            "module_name": "yjsexample.sample"
        }
    }
}
~~~

### /api/moduleClassInfo/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
获取给定包名和类名的类相关信息，包含类的签名，方法，和函数
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
module_name  | string  | 是  | Python module name
module_class_name  | string  | 是  | Python class name

####postman 请求参数示例
~~~
{
    "yjsJsonRpc": "0.1", 			
    "yjsMethod": "POST", 		
    "yjsParams": {		  		
        "module_name": "yjsexample.sample",
        "module_class_name": "B"
    },
    "yjsRequestId": "123456"	
}
~~~

####返回说明
~~~
{
    "yjsResponseId": "123456",
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "classInfo": {
            "class_func": [
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                },
                {
                    "func_name": "sayHello",
                    "func_sig": "(self, name)"
                }
            ],
            "class_method": [
                {
                    "method_sig": "()",
                    "method_name": "classMethod"
                }
            ],
            "class_name": "A",
            "class_sig": {
                "init_sig": "(self, age)"
            }
        }
    }
}
~~~

### /api/invokeModuleFunc/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
调用module的函数
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
package_name  | string  | 是  | Python package name
module_name  | string  | 是  | Python module name
module_func_name  | string  | 是  | Python function name
params | json 字典 | 否 | Python function arguments

####postman 请求参数示例
~~~
{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "package_name": "yjsexample",
            "module_name": "yjsexample.sample",
            "module_func_name": "moduleFunc",
            "params": {
            	"arg1":"string"
            }
        },
        "yjsRequestId": "123456"
}
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {	// 返回结果body
        "res": 1		// 返回结果实体
    },
    "yjsResponseId": "123456"
}
~~~


### /api/invokeModuleClzClassMethod/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
调用module 中指定class 的方法（用classmethod装饰器装饰）
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
package_name  | string  | 是  | Python package name
module_name  | string  | 是  | Python module name
module_class_name  | string  | 是  | Python class name
module_class_classmethod_name  | string  | 是  | Python class classmethod method name
params | json 字典 | 否 | Python class classmethod method arguments

####postman 请求参数示例
~~~
{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "package_name": "yjsexample",
            "module_name": "yjsexample.sample",
            "module_class_name": "A",
            "module_class_classmethod_name":"classMethod",
            "params": {
            	"arg1":"string"
            }
        },
        "yjsRequestId": "123456"
}
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "res": null
    },
    "yjsResponseId": "123456"
}
~~~
### /api/invokeModuleClzStaticMethod/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
调用module 中指定class 的函数（用staticmethod装饰器装饰）
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
package_name  | string  | 是  | Python package name
module_name  | string  | 是  | Python module name
module_class_name  | string  | 是  | Python class name
module_class_staticmethod_name  | string  | 是  | Python class staticmethod function name
params | json 字典 | 否 | Python class staticmethod function arguments

####postman 请求参数示例
~~~
{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "package_name": "yjsexample",
            "module_name": "yjsexample.sample",
            "module_class_name": "A",
            "module_class_staticmethod_name":"classStaticMethod",
            "params": {
            	"arg1":"string"
            }
        },
        "yjsRequestId": "123456"
}
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "res": null
    },
    "yjsResponseId": "123456"
}
~~~

### /api/createObj/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
创建python 的指定模块指定类的对象，返回对象id
该api的请求参数中所有参数名称为类签名中的参数名称，使用显示指定，参数value为存储在Python 执行程序存放的对象的id
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
package_name  | string  | 是  | Python package name
module_name  | string  | 是  | Python module name
module_class_name  | string  | 是  | Python class name
params | json 字典 | 否 | Python function arguments

####postman 请求参数示例
~~~
{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "package_name": "yjsexample",
            "module_name": "yjsexample.sample",
            "module_class_name": "A",
            "params": {
            	"age":"90fed962-211b-5614-90eb-bfe4c98f3cec"
            }
        },
        "yjsRequestId": "123456"
    }
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "objectId": "d2f3eb02-6106-54cb-b164-b0ffc9a16131"
    },
    "yjsResponseId": "123456"
}
~~~
### /api/createBuiltinsObj/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
调用python内置函数，创建python 基本类型对象，dict list string int 等
直接构造json对象，传值，注意null的处理(python 中为None)
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
params | json 字典 | 否 | Python builtins function arguments

####postman 请求参数示例
~~~
{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "params": {"a":1,"b":"addf"}
        },
        "yjsRequestId": "123456"
    }
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "objectId": "af3b033c-9e94-5e02-8fbe-97506c674d31"
    },
    "yjsResponseId": "123456"
}
~~~

### /api/objInfo/<objectId>/
####请求说明
* 请求方法 GET
* 请求参数格式 JSON

####接口描述
获取object的信息
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
objectId  | string  | 是  | yjs objectId
	

####postman 请求参数示例
~~~
postman get http://localhost:5000/api/objInfo/90fed962-211b-5614-90eb-bfe4c98f3cec/
~~~

####返回说明
~~~
{
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
~~~
### /api/invokeObjectGeneralMethod/
####请求说明
* 请求方法 POST
* 请求参数格式 JSON

####接口描述
调用对象的一般方法（具体到Python module class 中为function）
#### 参数说明
参数  | 类型 | 必须 | 说明
------------- | ------------- | ------------- | -------------
objectId  | string  | 是  | yjs objectId
object_method_name | string | 是 | yjs object method_name
params | json 字典 | 否 | Python function arguments

####postman 请求参数示例
~~~
d2f3eb02-6106-54cb-b164-b0ffc9a16131 为yjsexample.sample.A的对象id

{
        "yjsJsonRpc": "0.1",
        "yjsMethod": "POST",
        "yjsParams": {
            "objectId": "d2f3eb02-6106-54cb-b164-b0ffc9a16131",
            "object_method_name": "classGeneralMethod",
            "params": {
            }
        },
        "yjsRequestId": "123456"
}
~~~

####返回说明
~~~
{
    "yjsJsonRpc": "0.1",
    "yjsResult": {
        "res": "This is a general class method."
    },
    "yjsResponseId": "123456"
}
~~~
### /api/invokeBuiltinsMethod/
暂未支持