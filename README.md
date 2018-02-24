# pSQL_Log_Analysis

Summary: My python script uses psycopg2 to query a mock PostgreSQL database for
a fictional news website.  The news database is structured into 3 tables:
  1. articles,
  2. authors, and
  3. log
The article table includes several columns including title, slug (brief
description of the article), and id. The authors table includes an id,
article author name, and title. The log table includes a column for date, status
of the connection, and path to the article.

To use this script you will need a few requirements. You will need to use the
terminal. I am on a Windows machine so I used Git Bash. Its very nice. If you
are on a Linux or Mac your console is fine.
Download Git here: https://git-scm.com/downloads

Additionally, you will need to install VirtualBox, don't worry if you don't know
much about it. The other files will do all the heavy lifting. This will create
your Virtual Machine(VM)
Download VirtualBox here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Lastly, you will need to install Vagrant. Vagrant is software that configures
the VM and lets you share files between your host computer and
VM's file system.
Download Vagrant here: https://www.vagrantup.com/downloads.html

You still need to download the VM configuration.  you can do that by
following this link:
https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip

This will give you a directory called FSND-Virtual-Machine. Change to this
directory and look for another directory called Vagrant. While inside vagrant
type vagrant up, the VM will boot up. Then type vagrant ssh to run your new VM.

You will need the SQL database to use my script correctly. You can download it
here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
In this zip file move newsdata.sql into the vagrant directory.

Next you will need to load the data. Again, ssh into the VM. From there cd into
the vagrant directory by typing cd /vagrant. Once in there, type the command
'psql -d news -f newsdata.sql'
here is what that command does:
 - psql — the PostgreSQL command line program
 - -d news — connect to the database named news which has been set up for you
 - -f newsdata.sql — run the SQL statements in the file newsdata.sql

 Now, you should be able to fork my code and run log.py. 
