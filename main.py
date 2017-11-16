import dropbox


dbx = dropbox.Dropbox()
dbx.users_get_current_account()


for entry in dbx.files_list_folder('').entries:
    print(entry.name)