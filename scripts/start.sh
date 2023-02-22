python3 setup.py build_ext --inplace
python3 setup.py install
python3 -m unittest discover
pip3 install coverage
coverage run --source=. --omit=.venv/* -m unittest discover
coverage report -m
curl -Os https://uploader.codecov.io/latest/linux/codecov
chmod +x codecov
./codecov