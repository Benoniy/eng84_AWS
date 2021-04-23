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



## Step 3: