python3 setup.py build_ext --inplace
python3 setup.py install
python3 -m unittest discover
pip3 install coverage
coverage run -m unittest discover
bash <(curl -s https://codecov.io/bash) -t $CODECOV_TOKEN
