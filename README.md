# CS-8803-Data-Center-Project

## CloudLab SSH Instructions
- Use `ssh-keygen -t rsa` to generate key pairs on all/both nodes.
- Copy the public key from `.ssh/id_rsa.pub` and add it to ALL nodes' `.ssh/authorized_host` file using echo
