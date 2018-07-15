import sys
import dropbox




print ('Running')

dbx =dropbox.Dropbox('gVDYmXhB5sQAAAAAAAAXJ0EIQP8JyMyoDjC_9lZB5AHCsZpkNBeOb3NTYFfZ0-ZS')
curr_account = dbx.users_get_current_account()

shared_folder_name = 'EFG'

# Create a shared folder
launch = dbx.sharing_share_folder('/' + shared_folder_name)

if not launch.is_complete():
 print ('Shared folder creation failed, exiting')
 sys.exit(-1)

meta_data = launch.get_complete()

member_select = dropbox.sharing.MemberSelector.email('oh@isecthailand.com')
access_level = dropbox.sharing.AccessLevel.editor
add_member = dropbox.sharing.AddMember(member_select, access_level)

dbx.sharing_add_folder_member(meta_data.shared_folder_id, [add_member],
 custom_message="LETDO")

