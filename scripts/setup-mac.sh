echo "Installing tada-hdt-entity... "
wget https://github.com/oeg-upm/tada-hdt-entity/archive/v1.7.zip
unzip v1.7.zip
rm v1.7.zip
cd tada-hdt-entity-1.7;make install;cd ..;rm -Rf tada-hdt-entity-1.7