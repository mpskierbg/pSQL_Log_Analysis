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
much about it. The other files will do all the heavy lifting.
Download VirtualBox here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Lastly, you will need to install Vagrant. Vagrant is software that configures
the VirtualBox and lets you share files between your host computer and
VirtualBox's file system.
Download Vagrant here: https://www.vagrantup.com/downloads.html

You still need to download the VirtualBox configuration.  https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip
