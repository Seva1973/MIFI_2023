#!/bin/bash

# Создаем переменные для хранения путей к директориям которые будем архивировать
home_dir="/home/rvs/STUD/stud_bash"
remote_access_dir="/etc"
log_dir="/var/log"
backup_dir="/home/rvs/STUD/stud_bash/archive"

# Создаем архив с помощью утилиты tar
sudo tar -czf backup_cron.tar.gz $home_dir $remote_access_dir $log_dir

# Перемещаем созданный архив в директорию /archive
sudo mv backup_cron.tar.gz $backup_dir
