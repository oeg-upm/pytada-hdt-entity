// tnode.i - SWIG interface
%module entity
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_list.i"
%include "hdt.i"
%{
#include <HDTManager.hpp>
#include <easy_logger/easy_logger.h>
#include "entity.h"
%}
// Parse the original header file
%include "entity.h"
