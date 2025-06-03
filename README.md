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
# On each node make sure all other nodes are listed in
# /etc/hosts with their right hostnames
# A copy of the script must be present on each node with the 
# same path and filename
#
# To run it on on cluster
# mpiexec -hostfile ~/clusterfile python ./main.py
# or uv run main.py
###############################################################################

#Core Function   High-performance parallel computing over tightly-coupled nodes
#Transport Layer Shared memory, high-speed interconnects (InfiniBand, Ethernet)
#System Type     HPC clusters (e.g., scientific supercomputers)
#Libraries      OpenMPI, MPICH, Intel MPI (underlying mpi4py)


##############################################################################
