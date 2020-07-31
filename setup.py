# from distutils.core import setup, Extension
#
# modules = []
#
# # modules += [Extension('_tnode', ['tnode.i'], swig_opts=['-c++'])]
#
# # modules += Extension('_entity', ['entity.i'], swig_opts=['-c++'])
#
#
# entity_module = Extension('tada_hdt_entity._entity',
#                            include_dirs=['.'],
#                            libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
#                            extra_compile_args=['-std=c++11'],
#                            sources = ['entity.cpp','entity_wrap.cxx'])
#
#
# tnode_module = Extension('tada_hdt_entity._tnode',
#                     include_dirs = ['.'],
#                     libraries = ['hdt','easylogger','tadahdtentity','tabularparser'],
#                      extra_compile_args=['-std=c++11'],
#                     sources = ['tnode.cpp', 'tnode_wrap.cxx'])
#
#
# graph_module = Extension('tada_hdt_entity._graph',
#                     include_dirs = ['.'],
#                     libraries = ['hdt','easylogger','tadahdtentity','tabularparser'],
#                      extra_compile_args=['-std=c++11'],
#                     sources = ['graph.cpp','graph_wrap.cxx'])
#
#
# parser_module = Extension('tada_hdt_entity._parser',
#                     define_macros = [('MAJOR_VERSION', '1'),
#                                      ('MINOR_VERSION', '0')],
#                     include_dirs = ['.'],
#                     libraries = ['tabularparser'],
#                      extra_compile_args=['-std=c++11'],
#                     sources = ['parser.cpp', 'parser_wrap.cxx'])
#
#
# modules = [
#        parser_module,
#         tnode_module,
#        graph_module,
#        entity_module
# ]
#
# setup (name = 'tada_hdt_entity',
#        version = '1.5',
#        description = 'This package is a wrapper of tada_hdt_library',
#        author = 'Ahmad Alobaid',
#        author_email = 'aalobaid@fi.upm.es',
#        url = 'https://github.com/oeg-upm/pytada-hdt-entity',
#        long_description = '''This package is to label entity columns in CSV files using a given HDT file''',
#        ext_modules = modules,
#        # py_modules = ["entity","graph","tnode","parser"],
#        packages=['tada_hdt_entity'],
#        ext_package='tada_hdt_entity',
#        provides="tada_hdt_entity"
#        )

from distutils.core import setup, Extension

modules = []

# modules += [Extension('_tnode', ['tnode.i'], swig_opts=['-c++'])]

# modules += Extension('_entity', ['entity.i'], swig_opts=['-c++'])


entity_module = Extension('_entity',
                           include_dirs=['.'],
                           libraries=['hdt', 'easylogger', 'tadahdtentity', 'tabularparser'],
                           extra_compile_args=['-std=c++11'],
                           sources = ['entity.cpp','entity_wrap.cxx'])


tnode_module = Extension('_tnode',
                    include_dirs = ['.'],
                    libraries = ['hdt','easylogger','tadahdtentity','tabularparser'],
                     extra_compile_args=['-std=c++11'],
                    sources = ['tnode.cpp', 'tnode_wrap.cxx'])


graph_module = Extension('_graph',
                    include_dirs = ['.'],
                    libraries = ['hdt','easylogger','tadahdtentity','tabularparser'],
                     extra_compile_args=['-std=c++11'],
                    sources = ['graph.cpp','graph_wrap.cxx'])


parser_module = Extension('_parser',
                    include_dirs = ['.'],
                    libraries = ['tabularparser'],
                     extra_compile_args=['-std=c++11'],
                    sources = ['parser.cpp', 'parser_wrap.cxx'])


modules = [
    parser_module,
    tnode_module,
    graph_module,
    entity_module
]

setup (name = 'tada_hdt_entity',
       version = '1.7',
       description = 'This package is a wrapper of tada_hdt_library',
       author = 'Ahmad Alobaid',
       author_email = 'aalobaid@fi.upm.es',
       url = 'https://github.com/oeg-upm/pytada-hdt-entity',
       long_description = '''This package is to label entity columns in CSV files using a given HDT file''',
       ext_modules = modules,
       # py_modules = ["entity","graph","tnode","parser"],
       packages=['tada_hdt_entity'],
       ext_package='tada_hdt_entity',
       # provides="tada_hdt_entity"
)
