'''
# 获取函数参数列表中，每个参数的类型
# Name	                        kind        Meaning
# POSITIONAL_ONLY	            0           Value must be supplied as a positional argument.
                                            Python has no explicit syntax for defining positional-only parameters, but many built-in and extension module functions (especially those that accept only one or two parameters) accept them.
                                            POSITIONAL_ONLY 这类型在官方说明是不会出现在普通函数的，一般是内置函数什么的才会有，可能是self，cls或者是更底层的东西
# POSITIONAL_OR_KEYWORD	        1           Value may be supplied as either a keyword or positional argument (this is the standard binding behaviour for functions implemented in Python.)
# VAR_POSITIONAL	            2           A tuple of positional arguments that aren’t bound to any other parameter. This corresponds to a *args parameter in a Python function definition.
# KEYWORD_ONLY	                3           Value must be supplied as a keyword argument. Keyword only parameters are those which appear after a * or *args entry in a Python function definition.
                                            KEYWORD_ONLY 必须在 VAR_POSITIONAL 或 * 出现才能定义，否则为 POSITIONAL_OR_KEYWORD
# VAR_KEYWORD	                4           A dict of keyword arguments that aren’t bound to any other parameter. This corresponds to a **kwargs parameter in a Python function definition.
'''
'''
data的格式由 java 和 python 互操作规范来约定。
约定如下：
    data的格式为：
        "params": {
                "arg1": "object_id1",
                "arg2": "object_id2"
        }
'''

# 只有顶层需要约束传输方式，具体里面的内容，不关注，判断是否能执行时，也只关注参数类型
# 至于具体执行，出现什么错误，后续错误抛出，也跟这里没有关系
# 只做参数顺序转换，具体参数应该怎么传到函数中，不在此模块



from yjspymanager.objmanager import ObjManager


def get_method_input_args(params):
    '''
    获取参数名为key的对应对象id的python object,构造一个完整的python对象.

    hint: 需要考虑参数顺序,但使用显式参数命名，不需要考虑参数放置顺序

    get_method_input_args 仅处理非内建对象参数

    如果对象不存在，参数不应该放置None，json对象为null，也不把对应参数放到参数列表中

    '''

    arguments = {}
    for k, v in params.items():
        try:
            object = ObjManager.getObject(str(v))
            if object:
                arguments[k] = object
        except:
            continue
    return arguments
