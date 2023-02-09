// tnode.i - SWIG interface
%module graph
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_list.i"
%{
#include <easy_logger/easy_logger.h>
#include "graph.h"
%}
// Parse the original header file
%include "graph.h"
