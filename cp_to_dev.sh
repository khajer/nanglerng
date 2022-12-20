#media
rsync -r ubuntu@ec2-54-251-220-210.ap-southeast-1.compute.amazonaws.com:~/nanglerng/media ./nanglerng
#database (sqlite3)
rsync ubuntu@ec2-54-251-220-210.ap-southeast-1.compute.amazonaws.com:~/nanglerng/db.sqlite3 ./nanglerng/db.sqlite3

54.251.220.210
