rm -Rf dist
python setup.py bdist sdist
python setup.py bdist_rpm
python setup.py bdist_dumb

twine check dist/*
twine upload dist/*