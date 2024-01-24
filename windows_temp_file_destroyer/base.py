import shutil
from os import listdir, unlink
from os.path import isdir, isfile, islink, join
from tkinter.messagebox import askyesno, showerror, showinfo

TEMPPATH: str = "C:\\Windows\\Temp"


def delete_temp_files() -> None:
    items_found: dict = list_files()
    total_count: int = (
        len(items_found["files"])
        + len(items_found["links"])
        + len(items_found["dirs"])
    )

    if total_count > 0:
        answer: bool = askyesno(
            title="Confirm Deletion",
            message=(
                f"{total_count} item(s) found.\n\n"
                f'• {len(items_found["files"])} file(s)\n'
                f'• {len(items_found["links"])} links(s)\n'
                f'• {len(items_found["dirs"])} folders(s)\n\n'
                f"Do you want to delete them?"
            ),
        )

        if answer:
            deleted_count: int = 0

            for file in items_found["files"]:
                try:
                    unlink(join(TEMPPATH, file))
                    deleted_count += 1
                except Exception as e:
                    showerror(
                        title="Error Deleting Files",
                        message=(
                            f"Failed to delete {join(TEMPPATH, file)}. " f"{e}"
                        ),
                    )
                    pass

            for link in items_found["links"]:
                try:
                    unlink(join(TEMPPATH, link))
                    deleted_count += 1
                except Exception as e:
                    showerror(
                        title="Error Deleting Files",
                        message=(
                            f"Failed to delete {join(TEMPPATH, link)}. " f"{e}"
                        ),
                    )
                    pass

            for dir in items_found["dirs"]:
                try:
                    shutil.rmtree(join(TEMPPATH, dir))
                    deleted_count += 1
                except Exception as e:
                    showerror(
                        title="Error Deleting Files",
                        message=(
                            f"Failed to delete {join(TEMPPATH, dir)}. " f"{e}"
                        ),
                    )
                    pass

            showinfo(
                title="Process Complete",
                message=(
                    f"Deleted {deleted_count}/{total_count} "
                    f"items from {TEMPPATH}."
                ),
            )
    else:
        showerror(
            title="Error Deleting Files",
            message=f"No items found in {TEMPPATH}",
        )


def list_files() -> dict:
    items: dict = {"files": [], "links": [], "dirs": []}
    for item in listdir(TEMPPATH):
        if isfile(join(TEMPPATH, item)):
            items["files"].append(item)
        elif islink(join(TEMPPATH, item)):
            items["links"].append(item)
        elif isdir(join(TEMPPATH, item)):
            items["dirs"].append(item)

    return items
