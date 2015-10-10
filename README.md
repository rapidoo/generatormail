# pdfgenerator

System Dependencies on Ubuntu 14

sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

sudo apt-get install python-pip
sudo apt-get install libjpeg-dev
sudo apt-get install python-dev

sudo apt-get install default-jre

# to deploy
sudo apt-get install git


# App dependencies

pip install cassandra-driver
pip install flask
pip install flask_mail
pip install pyexcel
pip install pyexcel-xls

pip install flask_excel
pip install xhtml2pdf
pip install boto
pip install xlutils



# install cassandra
wget http://apache.websitebeheerjd.nl/cassandra/2.2.2/apache-cassandra-2.2.2-bin.tar.gz
gzip -d apache-cassandra-2.2.2-bin.tar.gz
tar xvf apache-cassandra-2.2.2-bin.tar


# install the demo app
https://github.com/rapidoo/generatormail.git


# to start to app

./apache-cassandra-2.2.2/bin/cassandra
./apache-cassandra-2.2.2/bin/cqlsh

# init keyspace and table
CREATE KEYSPACE simplex WITH replication         = {'class':'SimpleStrategy', 'replication_factor':1};

CREATE TABLE simplex.marvels2 (  name text PRIMARY KEY,         description text,         available text     );

#populate database
cd generatormail

python pop.py


#start webserver
python server.py

