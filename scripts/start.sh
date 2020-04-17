mkdir tada_hdt_entity
touch tada_hdt_entity/__init__.py
cp entity.py graph.py tnode.py parser.py tada_hdt_entity/
python setup.py build_ext --inplace
python setup.py install
