# PyBackup
# A program used for making backups of files and directories.


# HOW TO RUN
#
# python path_to_PyBackup.py source_path destination_path mode
#
# Arg 1: Path to the PyBackup.py file.
# Arg 2: Path to the directory you want to backup (can have subdirectories)
# Arg 3: Where to backup to.
# Arg 4: Which mode to use. Default is 1 (Copy).
#
# Paths should be absolute, and inside quotation marks ("").


# MODES
#
# Copy (default)    - Files are copied from source to destination, nothing gets deleted. This is the default mode.
# Clone             - Files are copied from source to destination, files in destination but not source get deleted (BEWARE!).


# EXAMPLES
#
# python \PyBackup\PyBackup.py "\SourceFolder" "\DestinationFolder" copy
# python \PyBackup\PyBackup.py "\SourceFolder" "\DestinationFolder" clone

###############################################################################


import os
import sys
import shutil

#"D:\_Mappar\Programmering\Python\Program\Egna Program\PyBackup\Test\Source"
#"D:\_Mappar\Programmering\Python\Program\Egna Program\PyBackup\Test\Destination"

def backup(source_path, destination_path, mode):
    relative_path = ""

    for root, dirs, files in os.walk(source_path):
        if root != source_path:
            relative_path = os.path.join(relative_path, os.path.basename(root))

        # DIRECTORIES
        for dir in dirs: 
            destination_filepath = os.path.join(destination_path, relative_path)
            new_dir = os.path.join(destination_filepath, dir)

            # If the directory doesn't exist, create it
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

        # FILES
        for filename in files:
            source_filepath = os.path.join(root, filename)
            destination_filepath = os.path.join(destination_path, relative_path, filename)

            # If the file already exists
            if os.path.exists(destination_filepath):

                # Only copy if the source file is newer than the destination file
                if os.path.getmtime(source_filepath) > os.path.getmtime(destination_filepath):

                    # shutil.copy2 copies everything, including metadata
                    shutil.copy2(source_filepath, destination_filepath)

            else:
                # Create the first copy (backup) of the file
                shutil.copy2(source_filepath, destination_filepath)

args = sys.argv

if len(args) < 2:
    print("ERROR: Missing source and destination paths!\n")

elif len(args) == 2:
    print("ERROR: Missing destination path!\n")

else:
    source_path = args[1]
    destination_path = args[2]
    mode = "copy"

    if len(args) > 3:
        mode = args[3]

    backup(source_path, destination_path, mode)