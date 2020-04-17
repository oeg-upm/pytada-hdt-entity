apt-get -y install python-dev

echo "Installing tada-hdt-entity... "
wget https://github.com/oeg-upm/tada-hdt-entity/archive/v1.5.zip
unzip v1.5.zip
rm v1.5.zip
cd tada-hdt-entity-1.5;make install;cd ..;rm -Rf tada-hdt-entity-1.5

echo "update linker caches..."
ldconfig