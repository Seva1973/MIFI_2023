# Built the file with this command: docker build -t api_ag .
# api_ag is the image name
# Running: docker run api_ag

# running the container with parameters:
#  _testing_7_10 % docker run -d --name myapitestingcontainer -p 80:80  api_ag

Запуск файла с дополнительными параметрами.

docker run -d --name myapitestingcontainer -p 80:80  api_ag
b3a9414c9d9612c4b5f73b92349328480f4f6ad8cb684377f09891e5220e135e

-d running in the background
--name gives the name to the existing container
-p port on which the api is working for this container

Checking the structure of the container by its ID.

_testing_7_10 % docker exec -ti b3a9414c9d9612c4b5f73b92349328480f4f6ad8cb684377f09891e5220e135e /bin/sh
# ls
app  requirements.txt
# cd ..
# ls
bin  boot  code  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
#
*********************************************************************************************
После сборки контенера так выглядит список контейнеров докера:
docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                     PORTS                NAMES
b3a9414c9d96   api_ag         "uvicorn app.main:ap…"   5 minutes ago    Up 5 minutes               0.0.0.0:80->80/tcp   myapitestingcontainer
3e55908b97c3   api_ag         "uvicorn app.main:ap…"   8 minutes ago    Exited (0) 7 minutes ago                        compassionate_williamson
16c2d9a02e2f   a811803c6925   "uvicorn app.main:app"   10 minutes ago   Exited (0) 9 minutes ago                        hardcore_agnesi
2216d08f8054   37495b7daf93   "uvicorn app.main:app"   15 minutes ago   Created

Source: https://github.com/patrickloeber/python-docker-tutorial
