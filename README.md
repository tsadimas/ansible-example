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