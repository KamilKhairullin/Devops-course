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

