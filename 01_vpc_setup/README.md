# Setting up a VPC with 2 subnets!  

## Step 1: VPC setup  

1. The first step is to create the vpc in the "Your VPC's" section  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/vpc-1.jpg)


2. When making the VPC there are only two important options.  
    * `blue` - Make sure you choose a good name  
    * `red` - Your ipv4 CIDR must use 2 unique numbers followed by 2 zero's and then a /16  
    * We will use these numbers again later on so don't forget them  
    

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/vpc-2.jpg)  



## Step 2: Internet gateway assignment  

1. Navigate to the Internet Gateway section and create one. This has to be done in order to connect your vpc to the  
   internet!  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ig-1.jpg)  


2. It's important to again select an easily identifiable name.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ig-2.jpg)  


3. Once you have created it right-click on it in the list and attach it to your vpc. Be sure that you choose your  
   VPC in the dropdown options!  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ig-3.jpg)  



## Step 3 Create your subnets:  
### Public subnet:


1. First navigate to the subnet page and click the "create subnet" button.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/subnet-1.jpg)  


2. Next we have to again pick a suitable name and note a few important items.  
   * `red` - This is the IPV4 CIDR for the vpc that we made earlier.
   * `blue` - This is the IPV4 CIDR for this current subnet, the first two numbers of this must be the same as in  
     VPC IPV4. The third number must be unique, it can't be the same as another subnet you have created. The fourth  
     number must be 0. Finally we must follow that with /24.


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/subnet-2.jpg)  


### Private:


1. This repeat the steps above but make certain to use a unique value for `blue`.


## Step 4 Managing the route tables:  
### Public:

1. This a bit complicated, the first thing we have to do is go to the route table page and identify the one that is 
   attached to our vpc. We can do this by going through the unnamed ones and seeing if they are attached to our VPC.
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-1.jpg)  


2. I strongly suggest you rename this by clicking on the empty name field to `eng84_name_public_rt`.  


3. Next you're going to want to give this subnet internet access by going to routes and adding one.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-2.jpg)  


4. We will connect 0.0.0.0/0 to our internet gateway, it should be the only option available.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-3.jpg)  


5. Now we will go back to the page we were on before and associate our public subnet with this route table, start by  
   clicking on subnet associations and click on edit subnet associations.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-4.jpg)  
![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-5.jpg)  


### Private:  

1. Now we want to create a new route table for out DB with no access to the internet. We will start by clicking  
   create route table.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-6.jpg)  


2. Make certain that you attach it to your vpc.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-7.jpg)  


3. We will now associate our private subnet in the same way as we did before.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-8.jpg)  
![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/route-table-9.jpg)  


4. Congrats, your route tables are now setup.  


## Step 5 Instance Creation:  
### App:  

1. First we will start by launching a new instance.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-1.jpg)  


2. We must use Ubuntu 16.04, you can use the search bar to find it easily.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-2.jpg)  


3. We will use a free t2 micro.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-3.jpg)  


4. This is where the important stuff starts.  
   * `red` - This is your VPC selection, it must be set to your VPC.  
   * `blue` - This is your subnet selection, in this case it should be set to your public subnet.
   * `green` - This must be enabled so that your app has a public IPV4.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-4.jpg)  


5. The storage page should be left on all default settings.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-5.jpg)  


6. On the tags page you MUST add a Name tag with a sensible name.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-6.jpg)  


7. This is the second really important part.  
   * `red` - This should be set to a name for your security group.  
   * `blue` - This is your ssh connection you must change the source to My IP  
   * `green` - This rule adds http access to the app, type should be http source should be set to 0.0.0.0/0  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-7.jpg)  


8. On the Final page you can now click launch, you will be asked to select a key pair. Choose the existing  
   DevOpsStudent key pair and then confirm.  
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-8.jpg)  


9. Congratulations you App should now be setup!  


### DB:  

1. Repeat steps 1, 2 and 3 exactly the same as app.  


2. Now repeat step 4 but remember that in this case your subnet should be set to your private one.  


3. Next repeat steps 5 and 6 exactly the same as app.  


4. Now you must repeat step 7 but your rules should instead look like this.  
   * `red` - this allows the app to connect to db locally, the source should be set to the IPV4 of your public subnet.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/01_vpc_setup/images/ec2-db-rules.jpg)  


5. Now simply repeat step 8 and 9.




