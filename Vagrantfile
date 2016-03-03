# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Just to make sure we use Virtualbox as default provider.
  ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  # config.vm.box = "ubuntu/wily64"
  config.vm.box = "codescalers-wily.box"

  # Download from this URL if box is not found.
  config.vm.box_url = "http://files.codescalers.com/Images/Vagrant/ubuntu/codescalers-wily.box"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.56.101"


  config.vm.provider "virtualbox" do |vb|
    vb.name = "py101"

    # Customize the amount of memory on the VM:
    vb.memory = "1024"
    vb.cpus = 2
  end

  # Provisioning via SHELL script!
  config.vm.provision "shell", path: "provision.sh"

end
