
import import_test.package1 as tp
from import_test.base import B
import pkgutil
import os
import importlib
import inspect
import sys

# print(tp)
# print(dir(tp))
# print(tp.__name__)
#
# sys.exit()

def import_package(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
        # print(mod)
    return mod


# module = my_import('import_test.package1.package2')
# print(module)
# print(module.__path__)


def find_modules_from_package(package, result_list=None):
    if not isinstance(result_list, list):
        result_list = list()
    package_path = package.__path__
    for filefinder, name, ispkg in pkgutil.iter_modules(package_path):
        sub_module_name = "{}.{}".format(package.__package__, name)
        sub_module = importlib.import_module(sub_module_name)
        if ispkg:
            find_modules_from_package(sub_module, result_list)
        else:
            result_list.append(sub_module)
    return result_list

# ret = list()
# find_modules_from_package(tp, ret)
# print(ret)


def find_sub_classes_from_package(package, base_class, result_list=None):
    assert issubclass(base_class, object)
    if not isinstance(result_list, list):
        result_list = list()
    package_path = package.__path__
    for filefinder, name, ispkg in pkgutil.iter_modules(package_path):
        sub_module_name = "{}.{}".format(package.__package__, name)
        sub_module = importlib.import_module(sub_module_name)
        if ispkg:
            find_sub_classes_from_package(sub_module, base_class, result_list)
        else:
            for class_name, v_class in inspect.getmembers(sub_module, inspect.isclass):
                if issubclass(v_class, base_class) and v_class != base_class:
                    result_list.append(v_class)
    return result_list


ret = list()
find_sub_classes_from_package(tp, B, ret)
print(ret)
