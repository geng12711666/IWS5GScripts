# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:16:28 2023

@author: jng22
"""

import csv

siminfo_csvfilename = '../datafiles/NIST-SIMCARD-Info.csv'
filename = '../datafiles/oai_db-basic-blank.sql'
  
# Open file 
with open(siminfo_csvfilename) as csv_file:
    
    # Read in csv file of SIM card info
    csv_reader_obj = csv.reader(csv_file)
    
    
    # Get the column index of wanted headers
    element_headers = [];
    
    for row in csv_reader_obj:
        element_headers = row;
        break
    
    print(element_headers)
    idx_imsi = element_headers.index('NEW IMSI');
    idx_ki = element_headers.index('New Ki');
    idx_opc = element_headers.index('New OPC');
    idx_s_ip = element_headers.index('Static IP attached');
    #print("IMSI is at column :", idx_imsi)
    #print("Ki is at column :", idx_ki)
    #print("OPc is at column :", idx_opc)
    #print("Static IP is at column :", idx_s_ip)
    
    
    ## Start inserting SIM card information into the file
    ## Find the line number of iserting point -> copy the original file content
    ## -> insert the data -> write the new content to output file
    
    # Start inserting Authentication for Subscribed Sim PLMN UEs
    # Find the line number where we want to insert data
    
    search_sentence = '-- Authentication for Sim PLMN UEs --'
    searched_line_num = 0
    
    with open(filename, 'r') as testFile:
        for line_num, line in enumerate(testFile, 1):
            if search_sentence in line:
                searched_line_num = line_num
                break
       
    # Read in the original 
    with open(filename, 'r') as testFile:    
        #get all the contents with line
        contents = testFile.readlines()
    
    # Specify the output file name
    output_filename = 'oai_db-basic.sql'
    
    # Iterate over each row in the csv file using reader object
    for row in csv_reader_obj:
        # point to next line
        searched_line_num = searched_line_num+1
        # Insert the string. Remember to add the \n in the end
        append_string = 'INSERT INTO `AuthenticationSubscription` (`ueid`, `authenticationMethod`, `encPermanentKey`, `protectionParameterId`, `sequenceNumber`, `authenticationManagementField`, `algorithmId`, `encOpcKey`, `encTopcKey`, `vectorGenerationInHss`, `n5gcAuthMethod`, `rgAuthenticationInd`, `supi`) VALUES'+'\n'
        contents.insert(searched_line_num, append_string)
        append_string2 = '(\'' +row[idx_imsi]+ '\', \'5G_AKA\', \'' +row[idx_ki]+ '\', \'' +row[idx_ki]+ '\', \'{\\"sqn\\": \\"000000000020\\", \\"sqnScheme\\": \\"NON_TIME_BASED\\", \\"lastIndexes\\": {\\"ausf\\": 0}}\', \'8000\', \'milenage\', \'' +row[idx_opc]+ '\', NULL, NULL, NULL, NULL, \'' +row[idx_imsi]+ '\');'+'\n'
        searched_line_num = searched_line_num+1
        contents.insert(searched_line_num, append_string2)
        
    # Write the new content to the output file
    with open(output_filename, 'w') as testFile:    
        #write back
        testFile.writelines(contents)
    
    
    
    
    # Start inserting Session Management for Subscribed Sim PLMN UEs
    # Find the line number where we want to insert data
    search_sentence = '-- Session Management for Sim PLMN UEs --'
    searched_line_num = 0
    
    with open(output_filename, 'r') as testFile:
        for line_num, line in enumerate(testFile, 1):
            if search_sentence in line:
                searched_line_num = line_num
                break
       
    # Read in the original content
    with open(output_filename, 'r') as testFile:    
        #get all the contents with line
        contents = testFile.readlines()
    
    
    # Iterate over each row in the csv file using reader object
    # Roll back the reader to beginning of file and skip the header row
    csv_file.seek(0)
    next(csv_file)
    
    for row in csv_reader_obj:
        # point to next line
        searched_line_num = searched_line_num+1
        # Insert the string. Remember to add the \n in the end
        append_string3 = 'INSERT INTO `SessionManagementSubscriptionData` (`ueid`, `servingPlmnid`, `singleNssai`, `dnnConfigurations`) VALUES'+'\n'
        contents.insert(searched_line_num, append_string3)
        append_string4 = '(\'' +row[idx_imsi]+ '\', \'00101\', \'{\\"sst\\": 1, \\"sd\\": \\"16777215\\"}\',\'{\\"oai\\":{\\"pduSessionTypes\\":{ \\"defaultSessionType\\": \\"IPV4\\"},\\"sscModes\\": {\\"defaultSscMode\\": \\"SSC_MODE_1\\"},\\"5gQosProfile\\": {\\"5qi\\": 1,\\"arp\\":{\\"priorityLevel\\": 15,\\"preemptCap\\": \\"NOT_PREEMPT\\",\\"preemptVuln\\":\\"PREEMPTABLE\\"},\\"priorityLevel\\":1},\\"sessionAmbr\\":{\\"uplink\\":\\"1000Mbps\\", \\"downlink\\":\\"1000Mbps\\"},\\"staticIpAddress\\":[{\\"ipv4Addr\\": \\"' +row[idx_s_ip]+ '\\"}]},\\"ims\\":{\\"pduSessionTypes\\":{ \\"defaultSessionType\\": \\"IPV4V6\\"},\\"sscModes\\": {\\"defaultSscMode\\": \\"SSC_MODE_1\\"},\\"5gQosProfile\\": {\\"5qi\\": 2,\\"arp\\":{\\"priorityLevel\\": 15,\\"preemptCap\\": \\"NOT_PREEMPT\\",\\"preemptVuln\\":\\"PREEMPTABLE\\"},\\"priorityLevel\\":1},\\"sessionAmbr\\":{\\"uplink\\":\\"100Mbps\\", \\"downlink\\":\\"100Mbps\\"}}}\');'+'\n'
        searched_line_num = searched_line_num+1
        contents.insert(searched_line_num, append_string4)
        
    # Write the new content to the output file
    with open(output_filename, 'w') as testFile:    
        #write back
        testFile.writelines(contents)
    



# ## Iterate over each row in the csv 
# # file using reader object
# for row in csv_reader_obj:
#     print("let's extract some element here : ", row[idx_imsi], ", ", row[idx_s_ip])


# ## Find the line number of specific sentence in the file in order for adding text
# search_sentence = '-- Sim PLMN UEs --'
# filename = 'oai_db-basic.sql'

# with open(filename) as sqlFile:
#     for line_num, line in enumerate(sqlFile, 1):
#         if search_sentence in line:
#             print ('found at line:', line_num)



# ## Insert lines of text into the file
# with open(filename, 'r') as testFile:    
#     #get all the contents with line
#     contents = testFile.readlines()

# # append line
# append_string = 'LALALALALALA\n'
# contents.insert(searched_line_num+1, append_string) 
# append_string = 'It\'s neither man nor woman\n'
# contents.insert(searched_line_num+2, append_string) 

# with open(filename, 'w') as testFile:    
#     #write back
#     testFile.writelines(contents)



# ## This one is for fixed IP
# append_string3 = 'INSERT INTO `SessionManagementSubscriptionData` (`ueid`, `servingPlmnid`, `singleNssai`, `dnnConfigurations`) VALUES'+'\n'
# contents.insert(searched_line_num, append_string3)
# append_string4 = '(\'' +row[idx_imsi]+ '\', \'00101\', \'{\\"sst\\": 1, \\"sd\\": "1"}\',\'{\\"oai\\":{\\"pduSessionTypes\\":{ \\"defaultSessionType\\": \\"IPV4\\"},\\"sscModes\\": {\\"defaultSscMode\\": \\"SSC_MODE_1\\"},\\"5gQosProfile\\": {\\"5qi\\": 1,\\"arp\\":{\\"priorityLevel\\": 15,\\"preemptCap\\": \\"NOT_PREEMPT\\",\\"preemptVuln\\":\\"NOT_PREEMPTABLE\\"},\\"priorityLevel\\":1},\\"sessionAmbr\\":{\\"uplink\\":\\"330Mbps\\", \\"downlink\\":\\"330Mbps\\"},\\"staticIpAddress\\":[{\\"ipv4Addr\\": \\"' +row[idx_s_ip]+ '\\"}]}}\');'+'\n'







