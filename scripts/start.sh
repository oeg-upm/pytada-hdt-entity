python3 setup.py build_ext --inplace
python3 setup.py install
python3 -m unittest discover
pip3 install coverage
coverage run --source=. --omit=.venv/* -m unittest discover
curl -s https://codecov.io/bash > codecovpush.sh
chmod +x codecovpush.sh
./codecovpush.sh -t $CODECOV_TOKEN
