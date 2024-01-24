from os import listdir, unlink
from os.path import isdir, isfile, islink, join
from tkinter.messagebox import askyesno, showerror, showinfo
import shutil

TEMPPATH = 'C:\\Windows\\Temp'

def delete_temp_files():
    items_found = list_files()
    total_count = len(items_found['files']) + len(items_found['links']) + len(items_found['dirs'])
    if total_count > 0:
        answer = askyesno(title='Confirm Deletion',
                    message=f'{total_count} item(s) found.\n\n• {len(items_found['files'])} file(s)\n• {len(items_found['links'])} links(s)\n• {len(items_found['dirs'])} folders(s)\n\nDo you want to delete them?')
        if answer:
            deleted_count = 0
            for file in items_found['files']:
                try:
                    unlink(join(TEMPPATH, file))
                    deleted_count += 1
                except Exception as e:
                    showerror(title='Error Deleting Files',
                              message=f'Failed to delete {join(TEMPPATH, file)}. {e}')
                    pass
            for link in items_found['links']:
                try:
                    unlink(join(TEMPPATH, link))
                    deleted_count += 1
                except Exception as e:
                    showerror(title='Error Deleting Files',
                              message=f'Failed to delete {join(TEMPPATH, link)}. {e}')
                    pass
            for dir in items_found['dirs']:
                try:
                    shutil.rmtree(join(TEMPPATH, dir))
                    deleted_count += 1
                except Exception as e:
                    showerror(title='Error Deleting Files',
                              message=f'Failed to delete {join(TEMPPATH, dir)}. {e}')
                    pass
            showinfo(title='Process Complete',
                     message=f'Deleted {deleted_count}/{total_count} items from {TEMPPATH}.')
    else:
        showerror(title='Error Deleting Files',
                  message=f'No items found in {TEMPPATH}')

def list_files():
    items = {
        'files': [],
        'links': [],
        'dirs': []
    }
    for item in listdir(TEMPPATH):
        if isfile(join(TEMPPATH, item)):
            items['files'].append(item)
        elif islink(join(TEMPPATH, item)):
            items['links'].append(item)
        elif isdir(join(TEMPPATH, item)):
            items['dirs'].append(item)
    
    return items