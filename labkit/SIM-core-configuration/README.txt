##########################################################################################
#  Scripts in this direcotry is related to 5G Core and SIM database configuration        #
##########################################################################################


#### Add SIM card information to the core database sql file ####

# 1. If the SIM card information file is .xls file rather than csv, use the following 
#    command to convert to csv first. In our usecase, <xls file name> is NIST-SIMCARD-Info.xls
#    and <Output file name> is NIST-SIMCARD-Info.csv

xls2csv <xls file name>.xls | sed 's/\"//g' > <Output file name>.csv 

# 2. Change the siminfo_csvfilename variable to the Output file name from step 1 and execute
#    It will modify the blank sql file(oai_db-basic-blank.sql) with the SIM information

python3 add-sim-to-databasefile.py

# 3. Move the outputsql file to the directory path of 5G core database. In our case is /etc/conf/firecell/5G/cn/database

sudo mv oai_db-basic.sql /etc/conf/firecell/5G/cn/database/oai_db-basic.sql


TODO : Make a configuration file for python script(for the filename, directory path, etc) and combine step 2 & 3 with one command. So user do not have to open the file and modify the variables and execute multiple commands


