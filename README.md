# pytada-hdt-entity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764190.svg)](https://doi.org/10.5281/zenodo.3764190)

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
[install-script](https://github.com/oeg-upm/tada-web/blob/master/setup.sh)
* For other linux distro and macOS: 
use the debian script but update it with the equivalent command to install prerequisite packages

# To update the python library (from the updated c++ source code library)
1. You need to setup the following environment variables:
	* `export project_dir='.'`  (or the directory of the c++ source code)
	* `export LC_ALL=en_US.UTF-8` (needed for mac)
	* `export LANG=en_US.UTF-8` (needed for mac)
1. Generate the interface files:
	* `invoke copy` (only if you need to copy the source files to the current folder. If you copy the c++ files to this directory, you do not need to do it).
	* `invoke parser`
	* `invoke tnode`
	* `invoke graph`
	* `invoke entity`  
1. Copy the python files into the package:
	* `cp parser.py tada_hdt_entity/`
	* `cp tnode.py tada_hdt_entity/`
	* `cp graph.py tada_hdt_entity/`
	* `cp entity.py tada_hdt_entity/`
	

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


# To cite
```
@software{alobaid_ahmad_2020_3764190,
  author       = {Alobaid, Ahmad and
                  Corcho, Oscar},
  title        = {pytada-hdt-entity},
  month        = apr,
  year         = 2020,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3764190},
  url          = {https://doi.org/10.5281/zenodo.3764190}
}
```
