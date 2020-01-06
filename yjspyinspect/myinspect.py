import inspect

'''
# 获取函数签名的参数列表

# 获取函数参数列表中，每个参数的类型
# Name	                        Meaning
# POSITIONAL_ONLY	            Value must be supplied as a positional argument.
#                               Python has no explicit syntax for defining positional-only parameters, but many built-in and extension module functions (especially those that accept only one or two parameters) accept them.
# POSITIONAL_OR_KEYWORD	        Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.)
# VAR_POSITIONAL	            A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a *args parameter in a Python function definition.
# KEYWORD_ONLY	                Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a * or *args entry in a Python function definition.
# VAR_KEYWORD	                A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a **kwargs parameter in a Python function definition.
'''

def getMethodSigObj(method_obj):
    return inspect.signature(method_obj)


def sigParameter(method_obj):
    return getMethodSigObj(method_obj).parameters

'''
获取函数的相关信息
参数个数，各个参数的类型信息等
'''
def getFunctionCodeInfo():
    # TODO：函数详细使用信息，定制化的，超低优先级
    info = {}
    return info


def sigParameterInfo(sigParameters):
    # todo: 返回定制的参数信息，添加辅助不同语言使用者使用的提示信息，低优先级
    res = []
    for k, v in sigParameters.items():
        tmp = {}
        tmp[k] = v
        tmp["kind"] = v.kind
        res.append(tmp)
        print(k, v)

    return res


'''
# sig.bind()验证，通过返回True，失败返回False
'''
def is_match_sig_parameters(arguments, object_method_obj):
    methodSigObj = getMethodSigObj(object_method_obj)
    try:
        methodSigObj.bind(**arguments)
        return True
    except:
        # todo: 考虑在这里抛出异常信息，给使用，待功能较为完善，再统一日志输出方式，低优先级
        return False
