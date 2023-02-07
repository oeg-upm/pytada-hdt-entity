# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _entity
else:
    import _entity

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _entity.delete_SwigPyIterator

    def value(self):
        return _entity.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _entity.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _entity.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _entity.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _entity.SwigPyIterator_equal(self, x)

    def copy(self):
        return _entity.SwigPyIterator_copy(self)

    def next(self):
        return _entity.SwigPyIterator_next(self)

    def __next__(self):
        return _entity.SwigPyIterator___next__(self)

    def previous(self):
        return _entity.SwigPyIterator_previous(self)

    def advance(self, n):
        return _entity.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _entity.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _entity.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _entity.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _entity.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _entity.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _entity.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _entity:
_entity.SwigPyIterator_swigregister(SwigPyIterator)

class EntityAnn(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _entity.EntityAnn_swiginit(self, _entity.new_EntityAnn(*args))
    __swig_destroy__ = _entity.delete_EntityAnn

    def setHDT(self, arg2):
        return _entity.EntityAnn_setHDT(self, arg2)

    def getHDT(self):
        return _entity.EntityAnn_getHDT(self)

    def setLogger(self, arg2):
        return _entity.EntityAnn_setLogger(self, arg2)

    def annotate_column(self, *args):
        return _entity.EntityAnn_annotate_column(self, *args)

    def annotate_semi_scored_column(self, *args):
        return _entity.EntityAnn_annotate_semi_scored_column(self, *args)

    def get_entities_of_value(self, *args):
        return _entity.EntityAnn_get_entities_of_value(self, *args)

    def get_leaf_classes(self, entity_uri):
        return _entity.EntityAnn_get_leaf_classes(self, entity_uri)

    def is_ancestor_of(self, a, b):
        return _entity.EntityAnn_is_ancestor_of(self, a, b)

    def get_tnode(self, uri):
        return _entity.EntityAnn_get_tnode(self, uri)

    def compute_intermediate_coverage(self, *args):
        return _entity.EntityAnn_compute_intermediate_coverage(self, *args)

    def compute_Ic_for_all(self):
        return _entity.EntityAnn_compute_Ic_for_all(self)

    def compute_Ic_for_node(self, tnode):
        return _entity.EntityAnn_compute_Ic_for_node(self, tnode)

    def compute_Lc_for_node(self, arg2):
        return _entity.EntityAnn_compute_Lc_for_node(self, arg2)

    def compute_Lc_for_all(self):
        return _entity.EntityAnn_compute_Lc_for_all(self)

    def compute_Is_for_all(self):
        return _entity.EntityAnn_compute_Is_for_all(self)

    def compute_Is_for_node(self, tnode):
        return _entity.EntityAnn_compute_Is_for_node(self, tnode)

    def compute_Ls_for_all(self):
        return _entity.EntityAnn_compute_Ls_for_all(self)

    def compute_Ls_for_node(self, tnode):
        return _entity.EntityAnn_compute_Ls_for_node(self, tnode)

    def get_graph(self):
        return _entity.EntityAnn_get_graph(self)

    def update_graph(self, *args):
        return _entity.EntityAnn_update_graph(self, *args)

    def compute_classes_entities_counts(self):
        return _entity.EntityAnn_compute_classes_entities_counts(self)

    def propagate_counts(self, tnode):
        return _entity.EntityAnn_propagate_counts(self, tnode)

    def compute_fs(self):
        return _entity.EntityAnn_compute_fs(self)

    def compute_fc(self, m):
        return _entity.EntityAnn_compute_fc(self, m)

    def compute_f(self):
        return _entity.EntityAnn_compute_f(self)

    def get_candidates(self):
        return _entity.EntityAnn_get_candidates(self)

    def pick_root(self):
        return _entity.EntityAnn_pick_root(self)

    def set_alpha(self, arg2):
        return _entity.EntityAnn_set_alpha(self, arg2)

    def get_alpha(self):
        return _entity.EntityAnn_get_alpha(self)

    def strip_quotes(self, arg2):
        return _entity.EntityAnn_strip_quotes(self, arg2)

    def get_quoted(self, arg2):
        return _entity.EntityAnn_get_quoted(self, arg2)

    def get_taged(self, arg2):
        return _entity.EntityAnn_get_taged(self, arg2)

    def recompute_f(self, arg2):
        return _entity.EntityAnn_recompute_f(self, arg2)

    def set_language_tag(self, arg2):
        return _entity.EntityAnn_set_language_tag(self, arg2)

    def set_title_case(self, arg2):
        return _entity.EntityAnn_set_title_case(self, arg2)

    def get_title_case(self, *args):
        return _entity.EntityAnn_get_title_case(self, *args)

    def annotate_entity_property_column(self, arg2, arg3, arg4):
        return _entity.EntityAnn_annotate_entity_property_column(self, arg2, arg3, arg4)

    def annotate_entity_property_pair(self, arg2, arg3):
        return _entity.EntityAnn_annotate_entity_property_pair(self, arg2, arg3)

    def annotate_entity_property_heuristic(self, arg2, arg3, arg4):
        return _entity.EntityAnn_annotate_entity_property_heuristic(self, arg2, arg3, arg4)

    def get_entities_of_class(self, arg2):
        return _entity.EntityAnn_get_entities_of_class(self, arg2)

    def get_properties_from_map(self):
        return _entity.EntityAnn_get_properties_from_map(self)

    def get_counts_of_class(self, arg2):
        return _entity.EntityAnn_get_counts_of_class(self, arg2)
    type_uri = property(_entity.EntityAnn_type_uri_get, _entity.EntityAnn_type_uri_set)
    subclassof_uri = property(_entity.EntityAnn_subclassof_uri_get, _entity.EntityAnn_subclassof_uri_set)
    delete_hdt_in_destructor = property(_entity.EntityAnn_delete_hdt_in_destructor_get, _entity.EntityAnn_delete_hdt_in_destructor_set)
    m_ambiguitity_penalty = property(_entity.EntityAnn_m_ambiguitity_penalty_get, _entity.EntityAnn_m_ambiguitity_penalty_set)

    def get_labels_uris(self):
        return _entity.EntityAnn_get_labels_uris(self)

    def append_label_uri(self, arg2):
        return _entity.EntityAnn_append_label_uri(self, arg2)

    def clear_label_uri(self):
        return _entity.EntityAnn_clear_label_uri(self)

    @staticmethod
    def file_exists(name):
        return _entity.EntityAnn_file_exists(name)

# Register EntityAnn in _entity:
_entity.EntityAnn_swigregister(EntityAnn)

def EntityAnn_file_exists(name):
    return _entity.EntityAnn_file_exists(name)


def abc():
    return _entity.abc()

def deref_list_string(l):
    return _entity.deref_list_string(l)
class MyObjectVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _entity.MyObjectVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _entity.MyObjectVector___nonzero__(self)

    def __bool__(self):
        return _entity.MyObjectVector___bool__(self)

    def __len__(self):
        return _entity.MyObjectVector___len__(self)

    def __getslice__(self, i, j):
        return _entity.MyObjectVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _entity.MyObjectVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _entity.MyObjectVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _entity.MyObjectVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _entity.MyObjectVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _entity.MyObjectVector___setitem__(self, *args)

    def pop(self):
        return _entity.MyObjectVector_pop(self)

    def append(self, x):
        return _entity.MyObjectVector_append(self, x)

    def empty(self):
        return _entity.MyObjectVector_empty(self)

    def size(self):
        return _entity.MyObjectVector_size(self)

    def swap(self, v):
        return _entity.MyObjectVector_swap(self, v)

    def begin(self):
        return _entity.MyObjectVector_begin(self)

    def end(self):
        return _entity.MyObjectVector_end(self)

    def rbegin(self):
        return _entity.MyObjectVector_rbegin(self)

    def rend(self):
        return _entity.MyObjectVector_rend(self)

    def clear(self):
        return _entity.MyObjectVector_clear(self)

    def get_allocator(self):
        return _entity.MyObjectVector_get_allocator(self)

    def pop_back(self):
        return _entity.MyObjectVector_pop_back(self)

    def erase(self, *args):
        return _entity.MyObjectVector_erase(self, *args)

    def __init__(self, *args):
        _entity.MyObjectVector_swiginit(self, _entity.new_MyObjectVector(*args))

    def push_back(self, x):
        return _entity.MyObjectVector_push_back(self, x)

    def front(self):
        return _entity.MyObjectVector_front(self)

    def back(self):
        return _entity.MyObjectVector_back(self)

    def assign(self, n, x):
        return _entity.MyObjectVector_assign(self, n, x)

    def resize(self, *args):
        return _entity.MyObjectVector_resize(self, *args)

    def insert(self, *args):
        return _entity.MyObjectVector_insert(self, *args)

    def pop_front(self):
        return _entity.MyObjectVector_pop_front(self)

    def push_front(self, x):
        return _entity.MyObjectVector_push_front(self, x)

    def reverse(self):
        return _entity.MyObjectVector_reverse(self)
    __swig_destroy__ = _entity.delete_MyObjectVector

# Register MyObjectVector in _entity:
_entity.MyObjectVector_swigregister(MyObjectVector)



