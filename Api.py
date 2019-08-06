import sys
import dropbox
import csv
import os

path= "/Users/sudhichaiungsuthornrungsi/GTS Dropbox/Sample Folder"

exampleFile = open('IEO2018list.csv')
exampleReader = csv.reader(exampleFile)
os.chdir(path)
dbx =dropbox.Dropbox('gVDYmXhB5sQAAAAAAAAXJ0EIQP8JyMyoDjC_9lZB5AHCsZpkNBeOb3NTYFfZ0-ZS')
curr_account = dbx.users_get_current_account()
access_level = dropbox.sharing.AccessLevel.editor
print ('Running')
for row in exampleReader:
    if exampleReader.line_num == 1 :
        continue
    print(str(row[1])+'_'+str(row[2][0]))
    shared_folder_name = str(row[1])+'_'+str(row[2][0])
    os.makedirs(shared_folder_name)
    launch = dbx.sharing_share_folder(path + shared_folder_name)
    meta_data = launch.get_complete()
    member_select = dropbox.sharing.MemberSelector.email('sutichaiu@gmail.com')
    add_member = dropbox.sharing.AddMember(member_select, access_level)
    dbx.sharing_add_folder_member(meta_data.shared_folder_id, [add_member], custom_message="LETSDO")


#shared_folder_name = 'Test1'

# Create a shared folder
# launch = dbx.sharing_share_folder('/' + shared_folder_name)
#
# if not launch.is_complete():
#  print ('Shared folder creation failed, exiting')
#  sys.exit(-1)
#
# print (curr_account)
#
# meta_data = launch.get_complete()
#
# # access_level = dropbox.sharing.AccessLevel.editor
# # add_member = dropbox.sharing.AddMember(member_select, access_level)
# #
# # dbx.sharing_add_folder_member(meta_data.shared_folder_id, [add_member], custom_message="LETDO")

