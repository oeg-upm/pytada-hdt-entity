// tnode.i - SWIG interface
%module tnode
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_list.i"
%{
#include "tnode.h"
%}
// Parse the original header file
%include "tnode.h"
