// entity.i - SWIG interface
%module entity
%include "std_string.i"
%include "std_unordered_map.i"
%include "std_list.i"
%include "cpointer.i"
%{
#include "entity.h"
#include "caster.h"
%}
// Parse the original header file
%include "entity.h"
%include "caster.h"

%template(MyObjectVector) std::list<string>;
%typemap(out) string {
   $result = SWIG_NewPointerObj($1, SWIGTYPE_p_string, 0);
}