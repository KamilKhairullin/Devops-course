## Best practices I used for Docker.

1. [hadolint](https://github.com/hadolint/hadolint) - helps to apply [best practices for Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) 

2. Add .dockerignore

3. Try to kepp your images as small as possible. Try ty use alpine images if it possible.

4. Use rootless containers - There are very few use cases where the container needs to execute as root, so don’t forget to include the USER instruction to change the default effective UID to a non-root user.

5.  Don’t bind to a specific UID - run the container as a non-root user, but don’t make that user UID a requirement.

6. Expose ports - Expose only the ports that your application needs and avoid exposing ports like SSH (22).

7. Don't use 
```
COPY . .
```
The “.” parameter is the build context. Using “.” as context is dangerous as you can copy confidential or unnecessary files into the container, like configuration files, credentials, backups, lock files, temporary files, sources, subfolders, dotfiles, etc.