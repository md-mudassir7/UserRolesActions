FastApi application which has users roles and resources collection

**Resources** collection holds the various resources existing(Example: EC2,S3,lambda)

**Roles** collection holds various actions that can be performed on the resources(Example: read->Ec2,List->S3,Write->lambda)

**Users** collection holds the list of various users with their names and the roles to which they have access to

The database Used is **MongoDB**

Use **MongoDB** compass for data visualisation

**How to use the code?**

1.Clone the respository
```
git clone https://github.com/mdmudassir7/UserRolesActions.git
```
2.Create a virtual environment
```
python -m venv env
```
3.Install the requirements
```
pip install -r requirements.txt
```
4.Run the server
```
uvicron main:app --reload
```