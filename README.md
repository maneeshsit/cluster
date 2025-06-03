# Assuming Raspbian, Ubuntu or Windows
#
# **Prerequisites**
#
# On every node:
# sudo apt-get update; sudo apt-get -y install python-mpi4py
# OR
# uv init.
# uv add mpi4py
# uv run main.py
# On master node
# ssh-keygen -t rsa
#
# For everynode: Replace IP-ADDRESS with IP of each node
# cat ~/.ssh/id_rsa.pub | ssh pi@IP-ADDRESS "cat >> .ssh/authorized_keys"
#
# Create cluster file on master node. One line per cluster.
