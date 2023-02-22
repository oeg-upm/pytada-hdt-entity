apt-get -y install python3-dev
apt-get -y install python3-pip
pip3 install -r requirements.txt
pip3 install coverage

echo "Installing tada-hdt-entity... "
wget https://github.com/oeg-upm/tada-hdt-entity/archive/v2.0.zip
unzip v2.0.zip
rm v2.0.zip
cd tada-hdt-entity-2.0;make install;cd ..;rm -Rf tada-hdt-entity-2.0

echo "update linker caches..."
ldconfig
