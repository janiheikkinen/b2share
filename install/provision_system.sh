#!/bin/bash

# # invoke with
# sudo /vagrant/provision_system.sh 2>&1 | tee provision.log

MYSQL_ROOT=invenio
USER=vagrant

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

echo; echo "### Stop iptables"
/etc/init.d/iptables stop
chkconfig iptables off

#echo; echo "### System update"
#yum -y update

echo; echo "### Install wget vim epel"
yum install -y wget vim epel-release

echo; echo "### Install lots of packages"
yum install -y screen strace openssl-devel \
           mysql mysql-devel sqlite-devel MySQL-python \
           python-pip python-chardet python-simplejson \
           pylint pyflakes python-BeautifulSoup python-devel \
           libxml2-devel libxml2-python libxslt-devel libxslt-python python-magic \
           gcc automake autoconf git gnuplot \
           redis python-redis \
           unzip bzip2-devel bzip2 xz-libs \
           java-1.7.0-openjdk-devel npm html2text netpbm giflib-devel \
           poppler ghostscript-devel gettext-devel \
           python-virtualenv python-virtualenvwrapper \
           libffi-devel

echo; echo "### Install mysql server"
rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
yum install -y mysql-server

echo; echo "### Groupinstall development"
yum groupinstall -y development

echo; echo "### Install bower and other tools"
npm install -g grunt grunt-cli bower less clean-css requirejs uglify-js

echo; echo "### Start redis"
chkconfig redis on
service redis start

echo; echo "### Start mysql"
chkconfig mysqld on
service mysqld start
mysqladmin -u root password $MYSQL_ROOT

echo; echo "### Make virtualenv b2share"
su $USER -c '
  sudo chown -R vagrant: /home/vagrant &&
  source /usr/bin/virtualenvwrapper.sh &&
  mkvirtualenv b2share && 
  workon b2share &&
  cdvirtualenv && 
  mkdir -p src/b2share;
  '

echo
echo " *** Please run ./install.sh to install B2SHARE in your new VM                  ***"
echo " *** If B2SHARE is already installed, go into the VM and you can start it with: ***"
echo " *** $ /vagrant/start_b2share.sh                                               #***"
