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


## Commands: 

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