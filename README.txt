Below is the description of files:

1. systeminfo.py > gives Linux system and running process information
2. systeminfo.sh > runs systeminfo.py file and appends output to logs.txt
3. windowsinfo.py > provides system and running process information 
4. logs.txt > It has stored information about system and processes.
5. jenkins.txt > pipeline syntax (sample)

Process and Steps :
> To run a job at a specific time, we need to setup cronjob :
  in Linux > crontab -e and provide the command and path
  in Windows > create schtasks or setup by Task scheduler
  
 > For automatic git action, setted up webhook in github and chosen GitHub hook trigger for GITScm polling in jenkins pipeline.

