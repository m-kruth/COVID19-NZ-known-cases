# Change Tracking Script

This script is intended to give us the ability to easily track which changes the MOH has made. This is how it works:

1. Copy and paste latest table from the MOH daily updates page (without table headings), into a .txt file (preferrably use the ISO date as the name) in the `/raw` subdirectory of the `MOH-daily-dumps` directory.
2. Edit the `reverse-file.py` script so that the `filename` variable matches the name of the file with the copy-pasted table.
3. Run the `reverse-file.py` python script. A file should be outputted to the `/parsed` subdirectory.
4. Perform a `git diff` operation passing in the names of current day and the previous day to check what the Ministry of health has changed.
