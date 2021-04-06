Procedure
* create an inventory file (e.g. hosts or hosts.yaml) that holds the remote hosts that ansible will handle.
* run 
```bash
ansible -m ping all
```
to check connectivity
* run testing environment
```bash
cd vagrant
vagrunt up
vagrant ssh-config >> ~/.ssh/config
```
* run a playbook
```bash
ansible-playbook -l database playbooks/database.yml
```

## Vault
* create a file that holds the **secret**
```bash
touch playbooks/vars/api_key.yml
```
* encrypt the file
```bash
ansible-vault encrypt playbooks/vars/api_key.yml
```
* run task that needs this file
```bash
ansible-playbook playbooks/use-api-key.yaml --ask-vault-pass
```
and you will be asked to provide the password
* edit the encrypoted file with
```bash
ansible-vault edit playbooks/vars/api_key.ym
```
* use stored password to decrypt
create a file that holds the password with 600 permissions
```bash
vim ~/.ansible/vault_pass.txt
chmod 600 ~/.ansible/vault_pass.txt
```
```bash
ansible-playbook playbooks/use-api-key.yaml --vault-password-file  ~/.ansible/vault_pass.txt
```


## Create self-signed certificates
```bash
cd files/certs
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 --nodes -subj '/C=GR/O=myorganization/OU=it/CN=myorg.com'
```
notice that crt and key files are added to .gitignore


* postgres
install postgresql role
```bash
ansible-galaxy install geerlingguy.postgresql
```
## Docker
```bash
ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip

```
## Jenkins
```bash
ansible-galaxy install geerlingguy.jenkins
ansible-galaxy install geerlingguy.java

```

## Links
* [apt module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
* [file module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html)
* [copy module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html)
* [service module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html)
* [debconf module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debconf_module.html)

* [ansible postgres role](https://galaxy.ansible.com/geerlingguy/postgresql)
