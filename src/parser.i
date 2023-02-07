// parser.i - SWIG interface
%module parser
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_list.i"
%{
#include "parser.h"
%}
// Parse the original header file
%include "parser.h"
