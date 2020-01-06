# standard library
import json
import sys

from flask import Flask
from flask import request

sys.path.append("../")

app = Flask(__name__)
# yjs diy library
from yjspyinspect import myinspect
from yjspyserialization import mySerialization
from yjspymanager.objmanager import ObjManager
from yjspymanager.packagemanager import PkgManager
from yjspymanager.modulemanager import ModuleManager


# ========
# =======package  module class func Info================
# ========

@app.route("/api/packageAllInfo/", methods=["POST"])
def getPackageTotalInfo():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "moduleInfo": ""
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        package_name = data["yjsParams"].get("package_name", None)
        if package_name:
            res["yjsResult"]["packageTotalInfo"] = PkgManager.packageInfo(package_name)
            return json.dumps(res)
        else:
            yjsError["message"] = "message lack"
            yjsError["data"] = "message lack"
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/availablePackages/", methods=["GET"])
def getAvailablePackages():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "moduleInfo": ""
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    res["yjsResult"]["availablePackages"] = PkgManager.availablePackages()
    return json.dumps(res)


@app.route("/api/availableModules/", methods=["GET"])
def getAvailableModules():
    '''
    返回所有可以使用的module
    '''
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "moduleInfo": ""
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    res["yjsResult"]["availableModules"] = PkgManager.availableModules()
    return json.dumps(res)


@app.route("/api/moduleInfo/", methods=["POST"])
def getModuleInfo():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "moduleInfo": ""
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }

    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        module_name = data["yjsParams"].get("module_name", None)
        if module_name:
            module_obj = ModuleManager.getModuleObj(module_name)
            if module_obj:
                res["yjsResult"]["moduleInfo"] = ModuleManager.getModuleInfo(module_obj)
                return json.dumps(res)
            else:
                yjsError["message"] = "module not found"
                yjsError["data"] = "module not found"
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "message lack"
            yjsError["data"] = "message lack"
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/moduleClassInfo/", methods=["POST"])
def getModuleClassInfo():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "moduleInfo": ""
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }

    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        module_name = data["yjsParams"].get("module_name", None)
        module_class_name = data["yjsParams"].get("module_class_name", None)
        print("moduleClassInfo_____________________________")
        print(module_name)
        print(module_class_name)
        if module_name and module_class_name:
            module_obj = ModuleManager.getModuleObj(module_name)
            if module_obj:
                class_obj = ModuleManager.getClassObj(module_obj, module_class_name)
                if class_obj:
                    res["yjsResult"]["classInfo"] = ModuleManager.getClassInfo(class_obj)
                    return json.dumps(res)
                else:
                    yjsError["message"] = "class not found"
                    yjsError["data"] = "class not found"
                    res["yjsError"] = yjsError
                    return json.dumps(res)
            else:
                yjsError["message"] = "module not found"
                yjsError["data"] = "module not found"
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "message lack"
            yjsError["data"] = "message lack"
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


# ===============invoke module general function=================
@app.route("/api/invokeModuleFunc/", methods=["POST"])
def invokeModuleFunc():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            "res": {}
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    # request1 = {
    #     "yjsJsonRpc": "0.1",
    #     "yjsParams": {
    #         "package_name": "",
    #         "module_name": "",
    #         "module_func_name": "",
    #         "params": {
    #             "arg1": "object_id1",
    #             "arg2": "object_id2"
    #         }
    #     },
    #     "yjsRequestId": "123456"
    # }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        package_name = data["yjsParams"]["package_name"]
        module_name = data["yjsParams"]["module_name"]
        module_func_name = data["yjsParams"]["module_func_name"]
        wrapped_object_params = data["yjsParams"]["params"]

        if module_func_name is None or module_name is None or package_name is None:
            yjsError["message"] = "message lack."
            yjsError["data"] = "message lack."
            res["yjsError"] = yjsError
            return json.dumps(res)

        # todo : 判断package or module 是否存在，不存在则从pip 或 第三方仓库 或 自建仓库 获取到这些package
        packageObj = PkgManager.getPackageObj(package_name)
        if packageObj is None:
            # 时间较长，直接抛出没有package
            # PkgManager.downloadPackage(package_name)
            # packageObj = PkgManager.getPackageObj(package_name)
            yjsError["message"] = "package not found."
            yjsError["data"] = "package not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        if PkgManager.hasModule(package_name, module_name) is None:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        module_obj = ModuleManager.getModuleObj(module_name)

        arguments = mySerialization.get_method_input_args(wrapped_object_params)

        if module_obj:
            module_func_obj = ModuleManager.getModuleFuncObj(module_obj, module_func_name)
            if module_func_obj:
                # 判断传入参数是否匹配 函数签名的参数，如果匹配则invoke method,否则抛出警告，错误或异常
                if myinspect.is_match_sig_parameters(arguments, module_func_obj):
                    res["yjsResult"]["res"] = module_func_obj(**arguments)
                    return json.dumps(res)
                else:
                    yjsError["message"] = "parameters is not match."
                    yjsError["data"] = "parameters is not match."
                    res["yjsError"] = yjsError
                    return json.dumps(res)
            else:
                yjsError["message"] = "module function is not found."
                yjsError["data"] = "module function is not found."
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method is error."
        yjsError["data"] = "request method is error."
        res["yjsError"] = yjsError
        return json.dumps(res)


# ===============invoke module classmethod function=============
@app.route("/api/invokeModuleClzClassMethod/", methods=["POST"])
def invokeModuleClzClassMethod():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            "res": {}
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    # request1 = {
    #     "yjsJsonRpc": "0.1",
    #     "yjsMethod": "POST",
    #     "yjsParams": {
    #         "package_name": "",
    #         "module_name": "",
    #         "module_class_name": "",
    #         "module_class_classmethod_name": "",
    #         "params": {
    #             "arg1": "object_id1",
    #             "arg2": "object_id2"
    #         }
    #     },
    #     "yjsRequestId": "123456"
    # }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        package_name = data["yjsParams"]["package_name"]
        module_name = data["yjsParams"]["module_name"]
        module_class_name = data["yjsParams"]["module_class_name"]
        module_class_classmethod_name = data["yjsParams"]["module_class_classmethod_name"]
        wrapped_object_params = data["yjsParams"]["params"]

        if module_class_classmethod_name is None or module_class_name is None or module_name is None or package_name is None:
            yjsError["message"] = "message lack."
            yjsError["data"] = "message lack."
            res["yjsError"] = yjsError
            return json.dumps(res)

        # todo : 判断package or module 是否存在，不存在则从pip 或 第三方仓库 或 自建仓库 获取到这些package
        packageObj = PkgManager.getPackageObj(package_name)
        if packageObj is None:
            # 时间较长，直接抛出没有package
            # PkgManager.downloadPackage(package_name)
            # packageObj = PkgManager.getPackageObj(package_name)
            yjsError["message"] = "package not found."
            yjsError["data"] = "package not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        if PkgManager.hasModule(package_name, module_name) is None:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        arguments = mySerialization.get_method_input_args(wrapped_object_params)

        moduleObj = ModuleManager.getModuleObj(module_name)
        if moduleObj:
            module_class_obj = ModuleManager.getClassObj(module_obj=moduleObj, class_name=module_class_name)
            if module_class_obj:
                module_class_classmethod_obj = ModuleManager.getClassMethodObj(module_class_obj,
                                                                               module_class_classmethod_name)
                if module_class_classmethod_obj:
                    # 判断传入参数是否匹配 函数签名的参数，如果匹配则invoke method,否则抛出警告，错误或异常
                    if myinspect.is_match_sig_parameters(arguments, module_class_classmethod_obj):
                        # invoke method
                        res["yjsResult"]["res"] = module_class_classmethod_obj(**arguments)
                        return json.dumps(res)
                    else:
                        yjsError["message"] = "parameters is not match."
                        yjsError["data"] = "parameters is not match."
                        res["yjsError"] = yjsError
                        return json.dumps(res)
                else:
                    yjsError["message"] = "class function is not found."
                    yjsError["data"] = "class function is not found."
                    res["yjsError"] = yjsError
                    return json.dumps(res)
            else:
                yjsError["message"] = "module class is not found."
                yjsError["data"] = "module class is not found."
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method is error."
        yjsError["data"] = "request method is error."
        res["yjsError"] = yjsError
        return json.dumps(res)


# ================invoke module class staticmethod function========
@app.route("/api/invokeModuleClzStaticMethod/", methods=["POST"])
def invokeModuleClassStaticMethod():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            "res": {}
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    # request1 = {
    #     "yjsJsonRpc": "0.1",ss
    #     "yjsMethod": "POST",
    #     "yjsParams": {
    #         "package_name": "",
    #         "module_name": "",
    #         "module_class_name": "",
    #         "module_class_staticmethod_name": "",
    #         "params": {
    #             "arg1": "object_id1",
    #             "arg2": "object_id2"
    #         }
    #     },
    #     "yjsRequestId": "123456"
    # }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        package_name = data["yjsParams"]["package_name"]
        module_name = data["yjsParams"]["module_name"]
        module_class_name = data["yjsParams"]["module_class_name"]
        module_class_staticmethod_name = data["yjsParams"]["module_class_staticmethod_name"]
        wrapped_object_params = data["yjsParams"]["params"]

        if module_class_staticmethod_name is None or module_class_name is None or module_name is None or package_name is None:
            yjsError["message"] = "message lack."
            yjsError["data"] = "message lack."
            res["yjsError"] = yjsError
            return json.dumps(res)

        # todo : 判断package or module 是否存在，不存在则从pip 或 第三方仓库 或 自建仓库 获取到这些package
        packageObj = PkgManager.getPackageObj(package_name)
        if packageObj is None:
            # 时间较长，直接抛出没有package
            # PkgManager.downloadPackage(package_name)
            # packageObj = PkgManager.getPackageObj(package_name)
            yjsError["message"] = "package not found."
            yjsError["data"] = "package not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        if PkgManager.hasModule(package_name, module_name) is None:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)

        arguments = mySerialization.get_method_input_args(wrapped_object_params)

        moduleObj = ModuleManager.getModuleObj(module_name)
        if moduleObj:
            module_class_obj = ModuleManager.getClassObj(module_obj=moduleObj, class_name=module_class_name)
            if module_class_obj:
                module_class_staticmethod_obj = ModuleManager.getClassFuncObj(module_class_obj,
                                                                              module_class_staticmethod_name)
                if module_class_staticmethod_obj:
                    # 判断传入参数是否匹配 函数签名的参数，如果匹配则invoke method,否则抛出警告，错误或异常
                    if myinspect.is_match_sig_parameters(arguments, module_class_staticmethod_obj):
                        # invoke method
                        res["yjsResult"]["res"] = module_class_staticmethod_obj(**arguments)
                        return json.dumps(res)
                    else:
                        yjsError["message"] = "parameters is not match."
                        yjsError["data"] = "parameters is not match."
                        res["yjsError"] = yjsError
                        return json.dumps(res)
                else:
                    yjsError["message"] = "class method is not found."
                    yjsError["data"] = "class method is not found."
                    res["yjsError"] = yjsError
                    return json.dumps(res)
            else:
                yjsError["message"] = "module class is not found."
                yjsError["data"] = "module class is not found."
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "module is not found."
            yjsError["data"] = "module is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method is error."
        yjsError["data"] = "request method is error."
        res["yjsError"] = yjsError
        return json.dumps(res)


# ===============module object =================================
@app.route("/api/createObj/", methods=["POST"])
def getObjectId():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "objectId": "041a6fad-baee-5d99-b680-57fc751d6278"
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }

    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }

    # request
    # {
    #     "yjsJsonRpc": "0.1",
    #     "yjsMethod": "POST",
    #     "yjsParams": {
    #         "package_name": "fake_package_name",
    #         "module_name": "fake_module_name",
    #         "module_class_name": "fake_module_class_name",
    #         "params": null
    #         "params": {
    #             "arg1": "object_id",
    #             "arg2": "object_id"
    #         }
    # },
    # "yjsRequestId": "123456"
    # }
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        print(data)
        if data is None:
            yjsError["message"] = "message lack"
            yjsError["data"] = "message lack"
            res["yjsError"] = yjsError
            return json.dumps(res)

        objectConfig = data["yjsParams"]
        package_name = objectConfig.get("package_name", None)
        # 注意module_name 需要约定填写成 package_name.parent_module_name.module_name
        module_name = objectConfig.get("module_name", None)
        class_name = objectConfig.get("module_class_name", None)

        if package_name is None or module_name is None or class_name is None:
            yjsError["message"] = "message lack"
            yjsError["data"] = "message lack"
            res["yjsError"] = yjsError
            return json.dumps(res)

        # todo : add top level arguments validate

        result = ObjManager.newObject(objectConfig)
        print("result====================================")
        if result is not None:
            res["yjsResult"]["objectId"] = result
            return json.dumps(res)
        else:
            yjsError["message"] = "object create fail"
            yjsError["data"] = "object create fail"
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/createBuiltinsObj/", methods=["POST"])
def getBuiltinsObj():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            # "objectId": "041a6fad-baee-5d99-b680-57fc751d6278"
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }

    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }

    # request = {
    #     "yjsJsonRpc": "0.1",
    #     "yjsMethod": "POST",
    #     "yjsParams": {
    #         "module_class_name": "dict",
    #         "params": {"a":"b","c":1}
    #         # "params": [1,2,3,4,5,6]
    #         # "params": "string"
    #     },
    #     "yjsRequestId": "123456"
    # }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        objectConfig = data["yjsParams"]
        class_name = objectConfig.get("module_class_name", None)
        # parames 如果传字符串或整型等对象初始化参数直接ok,如果parames 是None, 则不适用
        params = objectConfig.get("params", None)

        if class_name is None:
            if params is None:
                yjsError["message"] = "object create fail"
                yjsError["data"] = "lack necessary parameters or constructor function"
                res["yjsError"] = yjsError
                return json.dumps(res)
            else:
                result = ObjManager.newBuiltinsObjectWithoutBuiltinsFunction(params)
                if result is not None:
                    res["yjsResult"]["objectId"] = result
                    return json.dumps(res)
                else:
                    yjsError["message"] = "object create fail"
                    yjsError["data"] = "object create fail"
                    res["yjsError"] = yjsError
                    return json.dumps(res)
        else:
            result = ObjManager.newBuiltinsObjectWithBuiltinsFunction(class_name, params)
            if result is not None:
                res["yjsResult"]["objectId"] = result
                return json.dumps(res)
            else:
                yjsError["message"] = "object create fail"
                yjsError["data"] = "object create fail"
                res["yjsError"] = yjsError
                return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/objInfo/", methods=["POST"])
def getObjectInfo():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
        },
        "yjsResponseId": "123456"
    }

    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        objectId = data["yjsParams"].get("objectId", None)
        if objectId:
            if ObjManager.hasObject(objectId):
                obj = ObjManager.getObject(objectId)
                res["yjsResult"]["objectInfo"] = str(dir(obj))
                return json.dumps(res)
            else:
                yjsError["message"] = "object not found"
                yjsError["data"] = "object not found"
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "request argument lack"
            yjsError["data"] = "request argument lack"
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method error"
        yjsError["data"] = "request method error"
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/invokeObjectGeneralMethod/", methods=["POST"])
def invokeObjectGeneralMethod():
    res = {
        "yjsJsonRpc": "0.1",
        "yjsResult": {
            "res": {}
        },
        # "yjsError": {},
        "yjsResponseId": "123456"
    }
    yjsError = {
        "code": "30500",
        "message": "package not found",
        "data": {"info": "can not find package_name.", "hint": "please contact with administrator."}
    }
    # request1 = {
    #     "yjsJsonRpc": "0.1",
    #     "yjsMethod": "POST",
    #     "yjsParams": {
    #         "objectId": "",
    #         "object_method_name": "fake_object_method_name",
    #         "params": {
    #             "arg1": "object_id1",
    #             "arg2": "object_id2"
    #         }
    #     },
    #     "yjsRequestId": "123456"
    # }

    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf-8"))
        object_id = data["yjsParams"]["objectId"]
        object_method_name = data["yjsParams"]["object_method_name"]
        # 只记录一层<参数名，object_i> 的字典,然后调用相关方法构造python对象
        wrapped_object_params = data["yjsParams"]["params"]

        print("object_id", object_id)
        object_method_obj = ObjManager.getObjectMethodObj(object_id, object_method_name)
        print(object_method_obj)

        arguments = mySerialization.get_method_input_args(wrapped_object_params)
        if object_method_obj:
            # 判断传入参数是否匹配 函数签名的参数，如果匹配则invoke method,否则抛出警告，错误或异常
            if myinspect.is_match_sig_parameters(arguments, object_method_obj):
                # invoke method
                res["yjsResult"]["res"] = object_method_obj(**arguments)
                return json.dumps(res)
            else:
                yjsError["message"] = "parameters is not match."
                yjsError["data"] = "parameters is not match."
                res["yjsError"] = yjsError
                return json.dumps(res)
        else:
            yjsError["message"] = "method is not found."
            yjsError["data"] = "method is not found."
            res["yjsError"] = yjsError
            return json.dumps(res)
    else:
        yjsError["message"] = "request method is error."
        yjsError["data"] = "request method is error."
        res["yjsError"] = yjsError
        return json.dumps(res)


@app.route("/api/invokeBuiltinsMethod/", methods=["POST"])
def invokeBuiltinsMethod():
    pass


if __name__ == '__main__':
    app.run(debug=True)
