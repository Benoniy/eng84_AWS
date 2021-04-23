# Connecting to the instances I just made!  

## Connecting to the app:  
1. Connecting to the app is simple, it works in the exact same way that you are used to with only one minor  
   différance. We will be using the public ipv4 instead of a DNS link like usual. First select your app instance and  
   click connect.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-1.jpg)  


2. Next copy the command highlighted in red.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-2.jpg)  


3. Finally open a git bash shell and navigate to .ssh, then paste the command you copied.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-3.jpg)  


4. It should now connect, if you are asked to select yes/no/fingerprint type yes.  


5. If you are now in the shell then you have been successful.  



## Connecting to the db:  

1. This one is a little more complicated, as our db is not connected to the internet. We have to perform a proxy ssh.  


2. We will start by getting the public ipv4 of our app and noting it down.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-app-public.jpg)  


4. We now have to get the private ipv4 of our db instance.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-db-private.jpg)  


5. Using these two values we can now connect using a special ssh command in our git bash shell.  
   ```
   ssh -i ~/.ssh/DevOpsStudent.pem -o ProxyCommand="ssh -i ~/.ssh/DevOpsStudent.pem -W %h:%p ubuntu@app_ip" ubuntu@private
   ```


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/02_connecting/images/connect-db-connect.jpg)  


6. You should now be connected. Please note that you are not connected to the internet, so you can't run your provision  
   file.

