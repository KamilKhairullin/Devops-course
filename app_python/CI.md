# GitHub Actions best practices

## 1.  Keep your Actions minimal - 
github VMs are limited + you will wait more time wating 

## 2. Don’t install dependencies unnecessarily
avoid installing dependencies where you can.

## 3. Never hardcode secrets
GitHub Actions gives you encrypted secret handling. You can securely store secrets inside your repository’s settings, and then provide them as inputs or environment variables to your Actions at any time.

## 4. Limit environment variables to the narrowest possible scope
GitHub allows you to specify variables in the YML file for the Action or Workflow at any scope. For example, you are able to specify an environment variable at the workflow level that any job or step can access. However, if you specify an environment variable at the job or step level, the levels above that, like workflow, won’t be able to access it. 

# Jenkins

## 1. Create stage for evry major step
Two different steps: 
- install dependencies & run lint \ers and tests
- build docker image and push to dockerhub

## 2. Use environment instead of writing everything manually

## 3. Run multiple tasks in parallel 

## 4. Cleanup everything after all stages

## 5. Use Jenkins credentials for confidentional data
