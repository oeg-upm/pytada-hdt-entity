# pytada-hdt-entity
[![Build Status](https://ahmad88me.semaphoreci.com/badges/pytada-hdt-entity/branches/master.svg?style=shields&key=03f53198-0e20-470d-be7d-2ab289e1d436)](https://ahmad88me.semaphoreci.com/projects/pytada-hdt-entity)
[![codecov](https://codecov.io/gh/oeg-upm/pytada-hdt-entity/branch/master/graph/badge.svg?token=J3JDO36AWZ)](https://codecov.io/gh/oeg-upm/pytada-hdt-entity)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764190.svg)](https://doi.org/10.5281/zenodo.3764190)
[![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)


A python library binding of the c++ library [`tada-hdt-entity`](https://github.com/oeg-upm/tada-hdt-entity)


# Install
## Prerequisites to install
1. [hdt-cpp](https://github.com/rdfhdt/hdt-cpp)
2. [tabular_parser](https://github.com/ahmad88me/tabular-parser)
3. easy_logger lib
4. tada_hdt_entity lib
## Install via pip
```
pip install git+https://github.com/oeg-upm/pytada-hdt-entity.git
```

# Build and Compile
```
sh scripts/compile.sh  
```

[//]: # (# To build )

[//]: # (```)

[//]: # (python setup.py build_ext --inplace)

[//]: # (```)

[//]: # (*this will generate the .so library files*)

[//]: # (# Install )

[//]: # (```)

[//]: # (python setup.py install)

[//]: # (```)

[//]: # (*this will generate the python files for the library*)


# Install prerequisites via a script

**These are included in** `compile.sh`

* For debian and ubuntu: 
[install-script](https://github.com/oeg-upm/tada-api/blob/master/setup.sh)
* For other linux distro and macOS: 
use the debian script but update it with the equivalent command to install prerequisite packages

# To update the python library (from the updated c++ source code library)
1. You need to setup the following environment variables: **You might not need this in the newer versions**
	* `export project_dir='.'`  (or the directory of the c++ source code)
	* `export LC_ALL=en_US.UTF-8` (needed for mac)
	* `export LANG=en_US.UTF-8` (needed for mac)
1. Generate the interface files:
	* `invoke copyc` (only if you need to copy the source files to the current folder. If you copy the c++ files to this directory, you do not need to do it). Note that you need to setup the environment variable `project_dir` to point to the tada-hdt-entity directory.
1. Copy the python files into the package:
    * `invoke copypy` Copy the generated python files to tada_hdt_entity

[//]: # (	* `invoke parser`)

[//]: # (	* `invoke tnode`)

[//]: # (	* `invoke graph`)

[//]: # (	* `invoke entity`  )
[//]: # (1. Copy the python files into the package:)

[//]: # (	* `cp parser.py tada_hdt_entity/`)

[//]: # (	* `cp tnode.py tada_hdt_entity/`)

[//]: # (	* `cp graph.py tada_hdt_entity/`)

[//]: # (	* `cp entity.py tada_hdt_entity/`)
1. Update `setup.py` with the new version of the library	




# Prerequisites to build (from source)
1. SWIG (to handle .i files)
2. HDT lib
3. tabular_parser lib
4. easy_logger lib
5. tada_hdt_entity lib


## Install SWIG
### MacOS via brew
```brew install swig```

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

# Run tests
1. Generate `test.hdt`.
   1. `cd pytada-hdt-entity/test_files`
   2. `~/hdt-cpp/libhdt/tools/rdf2hdt test.ttl test.hdt` (change the location to point to the `hdt-cpp`).
2. Run test cases. 
   1. Return back to the pytada-hdt-entity folder `cd ..`.
   2. `python -m unittest discover`.

# Known Issues

* library not found.
`ld: library not found for -ltabularparser` (on Mac) when running  `python setup.py build_ext --inplace`.

Solution: Run `export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/lib` before running `python setup.py build_ext --inplace`.

* library linking error
```
In file included from graph.cpp:1:
./graph.h:8:10: fatal error: 'easy_logger/easy_logger.h' file not found
#include <easy_logger/easy_logger.h>
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
error: command '/usr/bin/clang' failed with exit code 1
``` (Mac)

