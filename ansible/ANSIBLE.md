# Lab 5. Install docker using ansible.

- step 1. In file *ssh_hosts.txt* add your host's address

- step 2. Install third-party roles
```
ansible-galaxy role install geerlingguy.docker geerlingguy.pip weareinteractive.apt
```
- step 3. Install docker to all your machines (aws_server group in my case)
```
ansible-playbook playbooks/install_docker.yml
```