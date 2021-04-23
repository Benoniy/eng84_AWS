# FAQ
***Thanks to Oleg for his help creating this FAQ!*** 

## How to transfer folder/file from local to cloud instance?

using scp command

1. Open terminal (for Mac and Linux users) or Git Bash shell (for Windows users)
   

2. Use this structure  
   `scp -ri <pem file path> <file/folder path> ubuntu@<ip only (withot http and slashes)>:<path on your cloud instance>`
   
example.

scp -i ~/.ssh/DevOpsStudent.pem /home/johndoe/Desktop/app ubuntu@10.10.110.1:/home/ubuntu

Cloning the repo from an online repository

1. Open terminal (for Mac and Linux users) or Bash sheel (for Windows users)
2. Clone the repo into your cloud instance using http protocol

git clone https://github.com/johndoe/online_repo.git  


## My provision.sh doesn't work, what do I do?  

1. First open it using `sudo nano provision.sh`  


2. If it says `Converted from DOS format` then this guide will help you. If it doesn't then seek help.  


3. Do the following commands in order:  
    1. `wget "http://ftp.de.debian.org/debian/pool/main/d/dos2unix/dos2unix_6.0.4-1_amd64.deb"`  
    2. `sudo dpkg -i dos2unix_6.0.4-1_amd64.deb`  
    3. `dos2unix provision.sh`
   
 
4. Your problem should now be solved!