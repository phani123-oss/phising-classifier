## Machine learning project

1. created an isolated environment which python==3.8
2. created requirements.txt,setup.py and all other folders
3. for running setup.py used pip install -e .
4. for requirements pip install -r requirements.txt
5. uploaded data into mongodb atlas using uploaddata to db
6. used aws for deploying 
7. after used aws to deploy 
         -- for aws use see security credentials like aws security key
         -- after scrolling our aws page we sey accesskey option
         -- click CLI then next then create accesskey
         -- create s3 bucket in aws
    Setting AWS_SECRET_ACCESS_KEY in environmental variables right click on windows tab->system->
    environmental variables->click new and set environmental variable 
8. next to run python app.py
9. used phisingtest.csv for upload in predict
10. to create docker image, type ECR in aws search box create repo (firstawsrepo) go to push commands
11. for using push commands we have to download docker desktop(docker engine must be running)
        -- we have our push commands in ECR repo page copy those links and paste it in vs code terminal 
        -- after refresh our ECR we have our latest image 
12. search for AWS app runner
        -- follow process deploy
        -- make sure delete all aws app runner,ecr,s3(empty,delete),security creadential acces key(deactivate,delete)

Note : rd /s /q .git(to remove .git directory)
git commits :
        -- git init
        -- git remote add origin https://github.com/your-username/your-repository.git
        -- git add .
        -- git commit -m "Initial commit"
        -- git push -u origin main

