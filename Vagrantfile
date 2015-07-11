# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "freefood89/nessiebox"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.ssh.insert_key = false
  config.ssh.forward_agent = true
end
