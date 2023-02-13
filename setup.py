from distutils.core import setup, Extension

# To solve the issue of Mac
include_dirs = ['.', '/usr/local/include/']

entity_module = Extension('_entity',
                          include_dirs=include_dirs,
                          libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                          extra_compile_args=['-std=c++11'],
                          sources=['src/entity.cpp', 'src/entity_wrap.cxx'])

tnode_module = Extension('_tnode',
                         include_dirs=include_dirs,
                         libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                         extra_compile_args=['-std=c++11'],
                         sources=['src/tnode.cpp', 'src/tnode_wrap.cxx'])

graph_module = Extension('_graph',
                         include_dirs=include_dirs,
                         libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                         extra_compile_args=['-std=c++11'],
                         sources=['src/graph.cpp', 'src/graph_wrap.cxx'])

parser_module = Extension('_parser',
                          include_dirs=include_dirs,
                          # libraries=['tabularparser', 'easylogger'],
                          libraries=['easylogger'],
                          extra_compile_args=['-std=c++11'],
                          sources=['src/parser.cpp', 'src/parser_wrap.cxx'])


modules = [
    parser_module,
    tnode_module,
    graph_module,
    entity_module
]

setup(name='tada_hdt_entity',
      version='1.10',
      description='This package is a wrapper of tada-hdt-entity',
      author='Ahmad Alobaid',
      author_email='aalobaid@fi.upm.es',
      url='https://github.com/oeg-upm/pytada-hdt-entity',
      long_description='''This package is to label entity columns in CSV files using a given HDT file''',
      ext_modules=modules,
      packages=['tada_hdt_entity'],
      ext_package='tada_hdt_entity'
)
