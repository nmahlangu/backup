import os, sys, time

start_time = time.time()

folders = ["Desktop/","Documents/","Developer/","Downloads/","Movies/","Music/","Pictures/"]
folder_path = "/Users/Nicholas/"
backup_path = "/Volumes/External\ HD/Backup\ Files/"

if not os.path.exists(backup_path.replace("\\","")):
	print "The backup volume External HD was not found, exiting..."
	sys.exit()
print "Beginning to write files to the volume External HD..."

# backup user folders
for i in range(len(folders)):
	os.system("sudo cp -R %s %s" % (folder_path+folders[i],backup_path+folders[i]))
	print "Copied files from %s to %s" % (folder_path+folders[i],backup_path+folders[i])

# store a list of installed applications
applications_path = "/Volumes/Macintosh HD/Applications/"
backup_list_path = backup_path + "applications.txt"
applications = filter(lambda x: x != ".localized" and x != ".DS_Store",os.listdir(applications_path))
if os.path.exists(backup_list_path.replace("\\","")):
	os.system("rm " + backup_list_path)
	print "Removed old application list at %s..." % backup_list_path
os.system("touch " + backup_list_path)
print "Created empty application list at %s..." % backup_list_path
for app in applications:
	os.system("echo %s >> %s" % (app,backup_list_path))
print "Wrote all installed applications to %s..." % backup_list_path

end_time = time.time()
print "Done backing up files! Script took %s minutes" % (end_time - start_time)

