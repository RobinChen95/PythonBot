import importlib
import pip
import pkgutil

'''
TODO： 一些信息是通过运行时获取的，后续根据时间添加本地pypi仓库后，将pypi入库即生成相关信息，存为静态，支持高效访问
# package or module 加入运行环境前，会inspect所有的信息，存数据库或文件，不在运行环境中运行时反射获取，优化访问
'''


class PkgManager:
    @staticmethod
    def isPackageExist(package_name):
        try:
            pkgobj = importlib.import_module(package_name)
            return True
        except:
            return False

    @staticmethod
    def downloadPackage(package_name):
        # 需要提前搭建pypi仓库
        # 下载package 到对应目录
        # python解释器将对应目录添加到Pythonpath中即可
        pass

    @staticmethod
    def getPackageObj(package_name):
        """ Import a module and return package object

        package must exists

        """
        if PkgManager.isPackageExist(package_name):
            try:
                return __import__(package_name, {}, {}, ["models"])
            except:
                return None
        else:
            return None

    @staticmethod
    def hasModule(package_name, module_name):
        packageObj = PkgManager.getPackageObj(package_name)
        if hasattr(packageObj, module_name):
            return True
        else:
            return False

    @staticmethod
    def packageInfo(package_name):
        res = {
            "package_name": package_name,
            "module_names": []
        }
        pkg_obj = PkgManager.getPackageObj(package_name)
        if pkg_obj:
            sub_modules = []
            for _, module_name, _ in pkgutil.walk_packages(pkg_obj.__path__, package_name + '.'):
                sub_modules.append(module_name)

            res["module_names"] = sub_modules
            return res
        else:
            return None

    @staticmethod
    def availablePackages():
        packages_path = ["/Users/mengliang/codeRepo/python_repo/SmartMove/PythonBot/diy-packages"]
        res = {
            "packages": ""
        }
        third_packages = []
        for _, package_name, _ in pkgutil.iter_modules(packages_path):
            third_packages.append(package_name)
        res["packages"] = third_packages
        return res

    @staticmethod
    def availableModules():
        packages_path = ["/Users/mengliang/codeRepo/python_repo/SmartMove/PythonBot/diy-packages"]
        # extend_path = ["/Users/mengliang/codeRepo/python_repo/SmartMove/PythonBot"]
        site_packages = ["/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages"]
        res = {
            "modules": ""
        }
        third_party_modules = []
        # bug: walk_packages executed may lead to unexpected error when it look for some path such as site-packages
        # todo: fix it
        for _, module_name, _ in pkgutil.walk_packages(packages_path):
            third_party_modules.append(module_name)

        res["modules"] = third_party_modules
        return res
