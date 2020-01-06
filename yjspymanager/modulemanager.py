import importlib.util
import inspect
import sys


class ModuleManager:
    @staticmethod
    def isModuleExists(module_name):
        module_spec = importlib.util.find_spec(module_name)
        if module_spec is None:
            return False
        else:
            return True

    @staticmethod
    def getModuleObj(module_name):
        # bug: 目前已知，重新加载模块，会影响shelve的序列化，如果创建对象和序列时的对象使用的module 对象不一样，则会导致序列化失败
        # todo: test 3-party pacakge module import . module_name 命名问题
        if module_name in sys.modules.keys():
            return sys.modules[module_name]

        module_spec = importlib.util.find_spec(module_name)
        if module_spec is None:
            return None
        module = importlib.import_module(module_name)

        # module = importlib.util.module_from_spec(module_spec)
        # module_spec.loader.exec_module(module)
        sys.modules[module_name] = module
        return module

    @staticmethod
    def loadModuleFromExtPath(ext_path, module_name):
        pass

    @staticmethod
    def getModuleClasses(module_obj):
        '''
        module_obj 必须被引入当前命名空间内
        '''
        res = []
        for k, v in inspect.getmembers(module_obj, predicate=inspect.isclass):
            # module_full_name = module_obj.__name__
            clz_info = {}
            clz_info["class_name"] = k
            # clz_info["module_full_name"] = module_full_name
            clz_info["class_sig"] = ModuleManager.getClassSig(v)
            clz_info["class_func"] = ModuleManager.getClassFuncInfo(v)
            clz_info["class_method"] = ModuleManager.getClassMethodInfo(v)
            res.append(clz_info)

        return res

    @staticmethod
    def getModuleFuncInfo(module_obj):
        '''
        module functions
        '''
        func_list = []
        for k, v in inspect.getmembers(module_obj, predicate=inspect.isfunction):
            func_info = {}
            func_info["func_name"] = k
            func_info["func_sig"] = ModuleManager.getModuleFuncSig(v)
            func_list.append(func_info)
        return func_list

    @staticmethod
    def getModuleInfo(module_obj):
        res = {}
        res["module_name"] = ModuleManager.getModuleName(module_obj)
        res["classes"] = ModuleManager.getModuleClasses(module_obj)
        res["module_func"] = ModuleManager.getModuleFuncInfo(module_obj)
        return res

    @staticmethod
    def getModuleName(module_obj):
        return module_obj.__name__
    @staticmethod
    def getClassObj(module_obj, class_name):
        for k, v in inspect.getmembers(module_obj, inspect.isclass):
            if class_name == k:
                return v
        return None

    @staticmethod
    def getClassInfo(class_obj):
        res = {}
        res["class_name"] = class_obj.__name__
        res["class_func"] = ModuleManager.getClassFuncInfo(class_obj)
        res["class_method"] = ModuleManager.getClassMethodInfo(class_obj)
        res["class_sig"] = ModuleManager.getClassSig(class_obj)
        return res

    @staticmethod
    def getClassFuncInfo(class_obj):
        '''
        初始化函数，构造函数, 普通函数, staticmethod装饰的方法
        '''
        res = []
        for k, v in inspect.getmembers(class_obj, inspect.isfunction):
            clz_method_info = {}
            clz_method_info["func_name"] = k
            clz_method_info["func_sig"] = ModuleManager.getClassFuncSig(v)
            res.append(clz_method_info)
        return res

    @staticmethod
    def getClassMethodInfo(class_obj):
        '''
         classmethod 装饰的方法bound method
         '''
        res = []
        for k, v in inspect.getmembers(class_obj, inspect.ismethod):
            clz_method_info = {}
            clz_method_info["method_name"] = k
            clz_method_info["method_sig"] = ModuleManager.getClassMethodSig(v)
            res.append(clz_method_info)

        return res

    @staticmethod
    def getClassFuncObj(class_obj, func_name):
        for name, func_obj in inspect.getmembers(class_obj, inspect.isfunction):
            if name == func_name:
                return func_obj
        return None

    @staticmethod
    def getClassMethodObj(class_obj, method_name):
        for name, method_obj in inspect.getmembers(class_obj, inspect.ismethod):
            if name == method_name:
                return method_obj
        return None

    @staticmethod
    def getModuleFuncObj(module_obj, func_name):
        for name, func_obj in inspect.getmembers(module_obj,inspect.isfunction):
            if name == func_name:
                return func_obj
        return None

    @staticmethod
    def getClassSig(class_obj):
        '''
        返回类的构造函数签名及初始化函数签名
        查看类有没有对应的__init__, __new__函数，没有，直接返回{}，否则返回__init__(__new__方法返回的是实例化的对象，init进行初始化操作)的函数签名
        远程调用者只需要知道初始化类实例的__init__的签名即可
        '''
        res = {}
        for k, v in inspect.getmembers(class_obj, predicate=inspect.isfunction):
            # if k == "__new__":
            #     res["new_sig"] = str(inspect.signature(v))
            if k == "__init__":
                res["init_sig"] = str(inspect.signature(v))
        return res

    @staticmethod
    def getClassMethodSig(method_obj):
        return str(inspect.signature(method_obj))

    @staticmethod
    def getClassFuncSig(func_obj):
        return str(inspect.signature(func_obj))

    @staticmethod
    def getModuleFuncSig(func_obj):
        return str(inspect.signature(func_obj))
