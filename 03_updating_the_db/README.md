# Updating the db instance!  

## Step 1 Give the database access to the internet:  

1. So first we will give the database access to the internet by going to our db security group and editing the rules.  
   Start by navigating to the security group section and then select the group, finally find the inbound rules and  
   edit them.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/03_updating_the_db/images/sg_1.jpg)  


2. Now we have to add a rule that allows the instance to access the internet purposes.  
    * `red` - Its important that we set the type to http and the source to 0.0.0.0/0

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/03_updating_the_db/images/sg_2.jpg)  


3. Next we have to navigate to the route table section of the AWS interface where we will change the subnet  
   associations of our public route table. After you select your public table click edit subnet associations.

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/03_updating_the_db/images/sg_3.jpg)  


4. Now associate both of your subnets with this table.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/03_updating_the_db/images/sg_4.jpg)  


5. You should now be able to connect to your normally using the same method you use to connect to your app  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/03_updating_the_db/images/sg_5.jpg)  


6. Now is the time for you to perform any actions you need to while this is connected to the internet.  


7. When you are done you now have to change all of these settings back so that your db is inaccessible again.  
