# How to run terraform

```
terraform init
```

```
terraform plan
```

```
terraform apply
```

- On macOS Big Sur 11.3 I have following error:

```
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[1],
│   on config.tf line 10, in resource "virtualbox_vm" "node":
│   10: resource "virtualbox_vm" "node" {
│ 
╵
╷
│ Error: [ERROR] Setup VM properties: exit status 1
│ 
│   with virtualbox_vm.node[0],
│   on config.tf line 10, in resource "virtualbox_vm" "node":
│   10: resource "virtualbox_vm" "node" {
│ 
╵
```

and destroy using 

```
terraform destroy
```
# Terraform best practices 

1. Don’t commit the .tfstate file

2. Back up your state files

3. Use variable files
```
terraform apply -var-file="testing.tfvars"
```

4. Stay up to date
```
terraform -v
```

5. Back up your system state
By default, the state of your environment is stored locally in your Terraform workspace directory in a file called terraform.tfstate along with a backup file called terraform.tfstate.backup.

