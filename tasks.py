from invoke import task

import os
project_dir = os.environ['project_dir']

@task
def copy(c):
    files = ["tnode.cpp", "tnode.h", "graph.cpp", "graph.h", "entity.cpp", "entity.h"]
    for f in files:
        fdir = os.path.join(project_dir, f)
        c.run("cp %s ./" % fdir)


@task
def parser(c):
    fname = "parser"
    cpp_name = "parser.cpp"
    comm = "swig -c++ -python %s.i ; " % fname
    comm += "g++ -O2 -std=c++11 -fPIC -c %s  ;" % cpp_name
    comm += "g++ -c -std=c++11 -fpic %s_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include`   ; " % fname
    comm += "g++ -lpython -std=c++11 -dynamiclib  %s.o %s_wrap.o -o _%s.so -leasylogger  -ltabularparser -pthread ;" % (fname, fname, fname)
    comm += "python %s_test.py " % (fname)
    print("command: ")
    print(comm)
    c.run(comm)


@task
def entity(c):
    fname = "entity"
    cpp_name = "entity.cpp"
    comm = "swig -c++ -python %s.i ; " % fname
    comm += "g++ -O2 -std=c++11 -fPIC -c %s  ;" % cpp_name
    comm += "g++ -c -std=c++11 -fpic %s_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include`   ; " % fname
    comm += "g++ -lpython -std=c++11 -dynamiclib  %s.o %s_wrap.o -o _%s.so -leasylogger -ltadahdtentity -lhdt -ltabularparser -pthread ;" % (fname, fname, fname)
    comm += "python %s_test.py " % (fname)
    print("command: ")
    print(comm)
    c.run(comm)


@task
def graph(c):
    tn = """
swig -c++ -python tnode.i
g++ -O2 -fPIC -c tnode.cpp 
g++ -O2 -fpic tnode_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include` 
g++ -lpython -dynamiclib -flat_namespace tnode.o tnode_wrap.o -o _tnode.so 
"""

    fname = "graph"
    cpp_name = "graph.cpp"
    comm = "swig -c++ -python %s.i ; " % fname
    comm += "g++ -O2 -std=c++11 -fPIC -c %s  ;" % cpp_name
    comm += "g++ -c -std=c++11 -fpic %s_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include`   ; " % fname
    comm += "g++ -lpython -std=c++11 -dynamiclib  %s.o %s_wrap.o -o _%s.so -leasylogger -ltadahdtentity ;" % (fname, fname, fname)
    comm += "python %s_test.py " % (fname)
    print("command: ")
    print(comm)
    c.run(comm)


@task
def tnode(c):


    ex = """
swig -c++ -python example.i
g++ -O2 -fPIC -c example.cxx
g++ -O2 -fPIC -c example_wrap.cxx -I/usr/include/python2.6
g++ -lpython -dynamiclib example.o example_wrap.o -o _example.so
    """
    tn = """
swig -c++ -python tnode.i
g++ -O2 -fPIC -c tnode.cpp 
g++ -O2 -fpic tnode_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include` 
g++ -lpython -dynamiclib -flat_namespace tnode.o tnode_wrap.o -o _tnode.so 
"""

    fname = "tnode"
    cpp_name = "tnode.cpp"
    extension_name = "tnode.so"
    comm = "swig -c++ -python %s.i ; " % fname
    comm += "g++ -O2 -std=c++11 -fPIC -c %s ;" % cpp_name
    comm += "g++ -c -std=c++11 -fpic %s_wrap.cxx -I/usr/include/python2.7  -I .  `python-config --include` ; " % fname
    # comm += "g++ -lpython -dynamiclib %s.o %s_wrap.o -o _%s.so ;" % (fname, fname, fname)
    comm += "g++ -lpython -std=c++11  -dynamiclib -flat_namespace %s.o %s_wrap.o -o _%s.so ;" % (fname, fname, fname)
    comm += "python tnode_test.py "
    print("command: ")
    print(comm)
    c.run(comm)


@task
def cpplib(c):
    c.run(
        "g++ -std=c++11  -c {0}/src/entity.cpp {1}/src/graph.cpp {2}/src/tnode.cpp {3}/src/main.cpp ; "
        "g++ -o tadaentity entity.o graph.o tnode.o main.o -lhdt -pthread -leasylogger -ltabularparser ; "
        "g++ -std=c++11    -dynamiclib -flat_namespace  {4}/src/entity.cpp {5}/src/graph.cpp {6}/src/tnode.cpp  -o libtadahdtentitypy.so -lhdt -pthread -leasylogger -ltabularparser"
        "".format(project_dir, project_dir, project_dir, project_dir, project_dir, project_dir, project_dir)
    )

@task
def pylib(c):
    # cpp_name = "example.cpp"
    cpp_name = "entity_wrapper.cpp"
    extension_name = "example.so"
    # comm = "g++  -Wall -shared -std=c++11 -fPIC -std=c++11 -dynamiclib -flat_namespace `python -m pybind11 --includes` /Users/aalobaid/workspaces/Cworkspace/tada-hdt-entity/src/entity.cpp example.cpp -o example.so"
    # comm += "  -lhdt -pthread -leasylogger -ltabularparser  -ltadahdtentity"
    comm = "g++ -Wall -shared -std=c++11 -fPIC -std=c++11 -dynamiclib -flat_namespace " \
        "`python -m pybind11 --includes` " \
        "-I /usr/include/python2.7 -I .  " \
        "{0} " \
        "-o {1} " \
        "-L. -ltadahdtentitypy -lhdt -pthread -leasylogger -ltabularparser -Wl,-rpath,.".format(cpp_name, extension_name)
    print("command: ")
    print(comm)
    c.run(comm)
    # -ltadahdtentitypy
    # c.run(
    #     "g++ -O3 -std=c++11 -dynamiclib -flat_namespace "
    #     "`python -m pybind11 --includes` "
    #     "-I /usr/include/python2.7 -I .  "
    #     "{0} "
    #     "-o {1} "
    #     "-L. -llibtadahdtentitypy -Wl,-rpath,.".format(cpp_name, extension_name)
    # )