# How do I add an NACL to my VPC?  

## Step 1 Create a NACL:  

1. Start by going to the VPC section and finding the Network ACL's section. Then click Create network ACL.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-1.jpg)  


2. Choose a convenient name for your NACL and make sure that you pick your VPC correctly.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-2.jpg)  


## Step 2 assign rules to the NACL:  

1. We now have to set our inbound rules, we will start by selecting our nacl and then clicking inbound rules. Next  
   select edit inbound rules.
   

![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-3.jpg)  


2. These rules each do different things each one we make should be set to allow.
    * `red` - This rule allows external http traffic to come in to the network, the type must be http and the source  
      must be 0.0.0.0/0
    * `blue` - This rule allow SSH connections to the VPC, the type must be http and the source must be either  
      0.0.0.0/0 or yourIp/32  
    *  `green` - This allows subnets within the VPC to talk to each other. The type should be All Traffic and the  
       source must be your VPC's IPV4 CDIR  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-4.jpg)  


3. Now we have to create our outbound rules by selecting outbound rules and then selecting edit outbound rules.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-5.jpg)  


4. There is only one rule here.  
    * `red` - This rule allows All Traffic out of the vpc. The type should be All Traffic and the source should be  
      0.0.0.0/0


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-6.jpg)  


## Step 3 assign subnets to the NACL:  

1. Now we have to assign our subnets to this NACL, we can do this by selecting and editing our subnet associations.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-7.jpg)  


2. Both of your subnets should be selected.  


![placeholder](https://github.com/Benoniy/eng84_AWS/blob/main/04_adding_nacl/images/nacl-8.jpg)  


3. Congratulation's if everything is still working then you are done.