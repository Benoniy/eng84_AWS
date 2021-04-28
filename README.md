## What is Cloud Computing?  
 ***Cloud Computing is the practise of outsourcing computer services from an external service provider to provide***  
 ***scalability and security.***  


## What are 3 benefits to Cloud Computing?  
1. Scalability  
2. Security  
3. Data Redundancy  


## What is AWS?
  ***Amazon Web Services (AWS) is an extension of amazon that provides cloud computing solutions to customers based***  
  ***on the scale of their problem. They can be used by larger organisations or even by single person. Within the***  
  ***industry they are the largest and most used provider of cloud computing services.***
  

## What are 3 benefits of using AWS?  
1. It has a lot of support since it is an industry standard  
2. Provides flexible solutions to multiple problems  
3. Amazon is so large that Data Backup and Security is a sure thing  


## What is a VPC:  
* Virtual Private Cloud defines a virtual network  
* Enables you to launch AWS instances resembling a traditional data center  
* Supports multiple subnets


## What are Subnets?  
* Sub-Networks make networks more efficient.  
* Defines a range of IP's  
* Can have specific rules based on route tables


## What are route tables?  
* Define the routes to and from one or more subnets.  
* Used for security
* Connect to the internet or to other subnets


## What is an internet gateway?  
* Connection point to the internet.  
* You attach to your VPC.


## What is an NACL?
* Basically functions as a port based firewall for the whole VPC.  
* Can be used for the whole VPC or a group of subnets.  
* Stateless  


## What is a Security Group?  
* Defines port based firewall rules.  
* Can be attached to one or more instances specifically.  
* Stateful.  


## Linux:  
* `man cmd` - Manual of the command
* `apt (install | remove)` - Package manager  
* `mkdir` - Make folder  
* `ls (-a)` - list files, -a shows all files  
* `nano` - text editor  
* `touch` - makefile  
* `cd` .. - up a dir  
* `pwd`  - print working directory  
* `mv` - move also used to rename  
* `cp` - copy  
* `rm` - remove  
* `ll` - check permissions  
* `chmod (+rwx | -rwx)` - change permissions  
  * `+ | -` - add or remove permission  
  * `r` - read permission  
  * `w` - write permission  
  * `x` - execute permission  
  * `777` - read, write and execute for everyone  
  * `400` - same as 777 but only for the issuing user  
  * `600` - same as 777 but only for the file owner and restricts all others  
  
* `top` - task manager  
* `kill pid` - Kills a process based on its pid  
* `sudo systemctl (status | start | stop | restart)` - Manage background services  
* Wildcards:  
  * `*` - All files  
  * `.` - Current folder  
  * `..` - Up one folder  
  
* `head` - prints first 10 lines of a file  
* `tail` - prints last 10 lines of a file  
* `sort` - sorts information in a file  
* `nl` - prints a file with numbered lines  
* `wc` - print out a word count  
* `cmd 1 | cmd 2` - Use command 1 and use that output as input for command 2  
* `cmd > file` - redirect output into a file and overwrite the contents  
* `cmd >> file` - redirect output into a file and append it to the end  


* Transfer files to the instance:  
  ```
  scp -ri ~/.ssh/.pem /file_to_transfer ubuntu@<ip>:~/location
  ```


* Fix DOS conversion error:
  ```
  wget "http://ftp.de.debian.org/debian/pool/main/d/dos2unix/dos2unix_6.0.4-1_amd64.deb"
  sudo dpkg -i dos2unix_6.0.4-1_amd64.deb
  ```


* Proxy SSH into our private network:  
  ```
  ssh -i ~/.ssh/local.pem -o ProxyCommand="ssh -i ~/.ssh/local.pem -W %h:%p ubuntu@app_ip" ubuntu@db_private_ip
  ```
  

## What is a bastion server?  
* Entry point into a VPC  
* Uses SSH agent forwarding  
* git bash ~/.bashrc (auto-sets parameters on Windows):  
```
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add ~/.ssh/DevOpsStudent.pem
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add ~/.ssh/DevOpsStudent.pem
fi

unset env
```
* git config: 
```
Host bastion
  Hostname public_ip
  User ubuntu
  IdentityFile ~/.ssh/.pem_file
  ForwardAgent yes
```


## Diagrams:  

![alt_text](https://github.com/Benoniy/eng84_AWS/blob/main/images/diagram.png)

![alt_text](https://github.com/Benoniy/eng84_AWS/blob/main/images/rules.jpg)



# What is S3?
* Simple Storage Service
* `aws configure` - setup
* `aws s3 mb s3://name` - make bucket
* `aws s3 rb s3://name` - delete bucket
* `aws s3 sync s3://name README.md` - Download
* `aws s3 linux_cmd s3://name/path` - This will mostly work