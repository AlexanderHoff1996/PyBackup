# PyBackup
A tool for making backups of your files

## HOW TO RUN

python path_to_PyBackup.py source_path destination_path mode

Arg 1: Path to the PyBackup.py file.
Arg 2: Path to the directory you want to backup (can have subdirectories)
Arg 3: Where to backup to.
Arg 4: Which mode to use. Default is 1 (Copy).

Paths should be absolute, and inside quotation marks ("").

## MODES

Copy (default)    - Files are copied from source to destination, nothing gets deleted. This is the default mode.
Clone             - Files are copied from source to destination, files in destination but not source get deleted (BEWARE!).

## EXAMPLES
```
python \PyBackup\PyBackup.py "\SourceFolder" "\DestinationFolder" copy
python \PyBackup\PyBackup.py "\SourceFolder" "\DestinationFolder" clone
```
