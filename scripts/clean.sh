pip uninstall tada_hdt_entity
rm -Rf *.cxx *.cpp *.o
rm -Rf src/*.cxx src/*.cpp src/*.o
rm -Rf src/graph.h src/tnode.h src/entity.h src/parser.h
rm -Rf tada_hdt_entity/tnode.py tada_hdt_entity/graph.py tada_hdt_entity/entity.py tada_hdt_entity/parser.py
rm -Rf build tada_hdt_entity/*.so *egg-info