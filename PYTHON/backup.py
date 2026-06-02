import shutil
import os

def backup_files(source_files, backup_folder):

    copied_files = set()

    # Create backup folder if it doesn't exist
    os.makedirs(backup_folder, exist_ok=True)

    with open("backup.log", "a") as log:

        for file in source_files:

            try:

                filename = os.path.basename(file)

                # Skip duplicates
                if filename in copied_files:
                    log.write(f"Skipped Duplicate: {filename}\n")
                    continue

                shutil.copy(file, backup_folder)

                copied_files.add(filename)

                log.write(f"Copied: {filename}\n")

            except FileNotFoundError:
                log.write(f"File Not Found: {file}\n")

            except PermissionError:
                log.write(f"Permission Denied: {file}\n")

    print("Backup Completed")


files = [
    "report.txt",
    "data.csv",
    "report.txt"
]

backup_files(files, "backup")