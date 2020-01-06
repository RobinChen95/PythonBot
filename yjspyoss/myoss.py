import uuid
import shelve


class PyOss:
    @staticmethod
    def insert(obj_hash_id, obj):
        d = shelve.open("./data.db", writeback=True)
        try:
            # print(type(obj_hash_id))
            # print(obj_hash_id, obj)

            # # shelve 不支持
            # print("select:", PyOss.select(obj_hash_id))
            # print("type:", type(obj))
            # print(d[obj_hash_id])
            print(obj)
            d[obj_hash_id] = obj
            print("select:", PyOss.select(obj_hash_id))

        except Exception as e:
            print(e)
            # print("insert fail")
            return None
        finally:
            d.close()
        return obj_hash_id

    @staticmethod
    def select(object_id):
        d = shelve.open("./data.db", flag='r')
        try:
            obj = d[object_id]
        except:
            return None
        finally:
            d.close()
        return obj

    @staticmethod
    def update(object_id, obj):
        d = shelve.open("./data.db", writeback=True)
        try:
            d[object_id] = obj
        except:
            return False
        finally:
            d.close()
        return True

    @staticmethod
    def delete(object_id):
        d = shelve.open("./data.db")
        try:
            obj = d[object_id]
            del obj
        finally:
            return True


class PyNamesapce:
    @staticmethod
    def getModuleNamespace(package_name, module_name):
        user_namespace = uuid.NAMESPACE_DNS
        name = package_name + module_name
        return uuid.uuid5(user_namespace, name)

    @staticmethod
    def getObjectHashId(module_namespace, obj):
        # todo: 分布式情况下，内存地址来确定Object uuid,会冲突的
        return str(uuid.uuid5(module_namespace, str(id(obj))))
