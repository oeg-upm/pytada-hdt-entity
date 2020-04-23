# pytada-hdt-entity
A python library binding of the c++ library `tada-hdt-entity`


# Install via pip
```
pip install git+https://github.com/oeg-upm/pytada-hdt-entity.git
```

# To build and install
```
python setup.py build_ext --inplace
python setup.py install
```

# Install prerequisites via a script
* For debian and ubuntu: 
[install-script](https://github.com/oeg-upm/tada-hdt-entity-experiment/blob/master/scripts/setup.sh)
* For other linux distro and macOS: 
use the debian script but update it with the equivalent command to install prerequisite packages



# Prerequisites to install
1. HDT lib
2. tabular_parser lib
3. easy_logger lib
4. tada_hdt_entity lib


# Prerequisites to build (from source)
1. SWIG (to handle .i files)
2. HDT lib
3. tabular_parser lib
4. easy_logger lib
5. tada_hdt_entity lib
