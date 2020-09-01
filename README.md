scp root@192.168.2.145:/mnt/user/appdata/degustibus/db.backup.5 ~/degustibus.db

scp -rp ./* root@192.168.2.145:~/degustibus
docker rm degustibus -f
cd degustibus/
docker build --tag degustibus:latest .
docker run -v /mnt/user/appdata/degustibus:/data --publish 6969:6969 --detach --name degustibus degustibus:latest

docker exec -it degustibus /bin/bash
... migrate


sysctl -w vm.max_map_count=262144


