echo 'Acquire::http::Proxy "http://apt.codescalers.com:8000";' > /etc/apt/apt.conf.d/90proxy.conf
apt-get update
apt-get install -y python3-pip
pip3 install ipython
