from distutils.core import setup, Extension

modules = []

entity_module = Extension('_entity',
                          include_dirs=['.', '/usr/local/include'],
                          library_dirs=['/usr/local/lib'],
                          libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                          extra_compile_args=['-std=c++11'],
                          sources=['entity.cpp'])

tnode_module = Extension('_tnode',
                         include_dirs=['.', '/usr/local/include'],
                         library_dirs=['/usr/local/lib'],
                         libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                         extra_compile_args=['-std=c++11'],
                         sources=['tnode.cpp'])

graph_module = Extension('_graph',
                         include_dirs=['.', '/usr/local/include'],
                         library_dirs=['/usr/local/lib'],
                         libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                         extra_compile_args=['-std=c++11'],
                         sources=['graph.cpp'])

parser_module = Extension('_parser',
                          include_dirs=['.', '/usr/local/include'],
                          library_dirs=['/usr/local/lib'],
                          libraries=['tabularparser', 'easylogger'],
                          extra_compile_args=['-std=c++11'],
                          sources=['parser.cpp'])

modules = [
    parser_module,
    tnode_module,
    graph_module,
    entity_module
]

setup(name='tada_hdt_entity',
      version='1.9',
      description='This package is a wrapper of tada-hdt-entity',
      author='Ahmad Alobaid',
      author_email='aalobaid@fi.upm.es',
      url='https://github.com/oeg-upm/pytada-hdt-entity',
      long_description='''This package is to label entity columns in CSV files using a given HDT file''',
      ext_modules=modules,
      # packages=['tada_hdt_entity'],
      # ext_package='tada_hdt_entity',
      )
