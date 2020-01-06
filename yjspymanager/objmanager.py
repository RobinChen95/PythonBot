import inspect

from yjspyinspect import myinspect
from yjspymanager.modulemanager import ModuleManager
from yjspyoss.myoss import PyOss, PyNamesapce
from yjspyserialization import mySerialization


class ObjManager:
    def __init__(self):
        pass

    @staticmethod
    def getObject(object_id):
        return PyOss.select(object_id)

    @staticmethod
    def hasObject(object_id):
        return PyOss.select(object_id)

    '''
    request
    {
        "yjsJsonRpc":"0.1",
        "yjsMethod":"POST",
        "yjsParams":{
            "package_name":"fake_package_name",
            "module_name":"fake_module_name",
            "module_class_name":"fake_module_class_name"
            "params":null
            "params":{
                "arg1":"object_id",
                "arg2":"object_id"
            }
        },
        "yjsRequestId":"123456" 
    }
    response
    {
        "yjsJsonRpc":"0.1",
        "yjsResult":{
            "objectId":"041a6fad-baee-5d99-b680-57fc751d6278"
        },
        "yjsError":{},
        "yjsResponseId":"123456"
    }
    response error
    {
        "yjsJsonRpc":"0.1",
        "yjsResult":{},
        "yjsError":{
            "code":"30500",
            "message":"package not found",
            "data":{"info":"can not find package_name.","hint":"please contact with administor."}
        },
        "yjsResponseId":"123456"
    }
    '''

    @staticmethod
    def newObject(objectConfig):
        package_name = objectConfig["package_name"]
        # 注意module_name 需要约定填写成 package_name.parent_module_name.module_name
        module_name = objectConfig["module_name"]
        class_name = objectConfig["module_class_name"]
        # parames 只记录一层<参数名，object_i> 的字典,然后调用相关方法构造python对象.
        # bug: 需要考虑参数顺序,应该将参数容器由字典变成列表
        parames = objectConfig.get("params", None)

        # test package import
        # bug fix , getModuleObj 返回已经import的的module_obj
        module_obj = ModuleManager.getModuleObj(module_name)
        module_namespace = PyNamesapce.getModuleNamespace(package_name, module_name)
        # todo 找不到class_obj、module_obj
        class_obj = ModuleManager.getClassObj(module_obj, class_name)
        if class_obj:
            # 如果有参数，则使用类的默认构造，参数不为空，需要约定使用参数的方式. 即需要处理传入参数中有其他对象的情况
            if parames:
                arguments = mySerialization.get_method_input_args(parames)
                print(arguments)
                obj = None
                if myinspect.is_match_sig_parameters(arguments, class_obj):
                    print("_+_+_+_+")
                    if parames is None:
                        obj = class_obj()
                    else:
                        try:
                            # 类的实例化，要看到是__init__的函数签名
                            obj = class_obj(**arguments)
                        except:
                            print("call constructor fail")
                            return None


            # todo: 出现异常，输出各种类型，这里的None的表达信息较少，不便于看清问题在哪
            obj_hash_id = PyNamesapce.getObjectHashId(module_namespace, obj)
            print(obj_hash_id)

            # todo: !!!!!!!!!!!! 注意如果reload module 会导致对象不一致，这个时候使用shelve会无法插入成功
            res = PyOss.insert(obj_hash_id, obj)
            print("res", res)
            return res
        else:
            return None

        # # TODO：test 不是内建属性，这里使用hasattr要注意会不会得到自己想要的结果
        # # class_obj
        # if hasattr(module_obj, class_name):
        #     class_obj = getattr(module_obj, class_name)
        #     # 如果参数为空，则使用类的默认构造，参数不为空，需要约定使用参数的方式. 即需要处理传入参数中有其他对象的情况
        #     arguments = mySerialization.get_method_input_args(parames)
        #     # todo : 判断传入参数是否匹配 类构造 签名的参数，如果匹配则invoke,否则抛出警告，错误或异常，下个计划fix
        #     print("_+_+_+_+")
        #     if parames is None:
        #         obj = class_obj(12)
        #         # print("+++++++++++++")
        #         # print(obj)
        #         # print(type(obj))
        #         # from yjsexample.sample import A
        #         # a = A(12)
        #         # print("type:  ", isinstance(a, A))
        #     else:
        #
        #         try:
        #             # 类的实例化，要看到是__init__的函数签名
        #             obj = class_obj(**arguments)
        #         except:
        #             return None
        #
        #     # todo: 出现异常，输出各种类型，这里的None的表达信息较少，不便于看清问题在哪
        #     obj_hash_id = PyNamesapce.getObjectHashId(module_namespace, obj)
        #     # print(obj_hash_id)
        #     # print("obj:", obj)
        #     # todo: !!!!!!!!!!!! 注意如果reload module 会导致对象不一致，这个时候使用shelve会无法插入成功
        #     res = PyOss.insert(obj_hash_id, obj)
        #     print(res)
        #     return res
        #
        # else:
        #     print("+_+++_++__+")
        #     return None
        #
        #
        #
        #     # user_namespace = uuid.NAMESPACE_DNS
        #     # name = package_name + module_name
        #     #
        #     # object_module_namespace = uuid.uuid5(user_namespace, name)
        #     #
        #     # # 实例化对象
        #     # # TODO : add package and module import
        #     # from yjsexample.sample import A
        #     # try:
        #     #     obj = A()
        #     #     hashid = uuid.uuid5(object_module_namespace, str(id(obj)))
        #     #
        #     #     d = shelve.open("./data.txt")
        #     #     try:
        #     #         objectId = str(hashid)
        #     #         d[objectId] = obj
        #     #     finally:
        #     #         d.close()
        #     #
        #     #     return objectId
        #     # except:
        #     #     return None

    @staticmethod
    def newBuiltinsObjectWithoutBuiltinsFunction(parames):
        var = parames

        module_namespace = PyNamesapce.getModuleNamespace("builtins", "builtins")

        obj_hash_id = PyNamesapce.getObjectHashId(module_namespace, var)

        return PyOss.insert(obj_hash_id, var)

    @staticmethod
    def newBuiltinsObjectWithBuiltinsFunction(class_name, parames):
        builtins_module_obj = ModuleManager.getModuleObj("builtins")
        if hasattr(builtins_module_obj, class_name):
            class_obj = getattr(builtins_module_obj, class_name)
            if parames is None:
                res = class_obj()
            else:
                res = class_obj(parames)

            module_namespace = PyNamesapce.getModuleNamespace("builtins", "builtins")

            obj_hash_id = PyNamesapce.getObjectHashId(module_namespace, res)

            return PyOss.insert(obj_hash_id, res)

        else:
            return None

    @staticmethod
    def updateObject(obj_id, object_info):
        # todo: complate this part. 根据object_info 对object进行更新

        newObj = PyOss.select(obj_id)
        return PyOss.update(obj_id, newObj)

    @staticmethod
    def getObjectType(object_id):
        pass

    @staticmethod
    def getObjectInfo(object_id):
        pass

    @staticmethod
    def isObjectMethodExist(object_id, method_name):
        if ObjManager.hasObject(object_id):
            if hasattr(ObjManager.getObject(object_id), method_name):
                return True
        return False

    @staticmethod
    def getObjectMethodObj(object_id, method_name):
        if ObjManager.hasObject(object_id):
            obj = ObjManager.getObject(object_id)
            print("get")
            print(obj)

            for name, method_obj in inspect.getmembers(obj):
                print(method_obj)
                if name == method_name:
                    return method_obj
        return None

        #
        # if ObjManager.hasObject(object_id):
        #     print(ObjManager.getObject(object_id))
        #     print()
        #     if hasattr(ObjManager.getObject(object_id), method_name):
        #         object_method_obj = getattr(ObjManager.getObject(object_id), method_name)
        #         return object_method_obj
        #     else:
        #         print("method obj get fail")
        #         return None
        # return None
