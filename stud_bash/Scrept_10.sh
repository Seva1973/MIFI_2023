#!/bin/bash
# 0) Записать выполнение скрипта bash
LOGFILE=/home/rvs/STUD/stud_bash/log.txt
# Открываем файл для записи лога и перенаправляем вывод скрипта в него
exec &> >(tee -a "$LOGFILE")
# Команды скрипта
echo "Начало выполнения скрипта"

# 1) Определение дистрибутива установленной операционной системы и версии дистрибутива и запись информации в отдельный файл
distro=$(lsb_release -i 2> /dev/null | awk '{print $3}')
version=$(lsb_release -r 2> /dev/null | awk '{print $2}')
echo "Distro: $distro" > /home/rvs/STUD/stud_bash/distro_version.txt
echo "Version: $version" >> /home/rvs/STUD/stud_bash/distro_version.txt

# 2) Проверка наличия репозитория Backports
if grep -q "backports" /etc/apt/sources.list; then
    echo "Репозиторий Backports уже добавлен"
else
    # Добавление репозитория Backports
    echo "Добавление репозитория Backports"
    echo "deb http://mirrors.kernel.org/ubuntu/ ${version}-backports main restricted universe multiverse" | sudo tee -a /etc/apt/sources.list
fi
# 3) Обновление списка репозиториев
sudo apt update
sudo apt upgrade -y

# 4) Установить и запустить Apache2 web server
sudo apt install -y apache2
sudo systemctl enable apache2
sudo systemctl start apache2

# 5) Установить Python
sudo apt install -y python3

# 6) Установить и запустить SSH server
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# 7) Второе обновление системы
sudo apt update
sudo apt upgrade -y

# 8) Очистка кэша пакетов, очистка ненужных пакетов, очистка зависимостей:
sudo apt clean
sudo apt autoclean
sudo apt autoremove

# 9) Создание нового пользователя rvs2 в новой директории home/rvs2 и нового пароля для rvs2
sudo useradd -m rvs2
sudo passwd rvs2

# 10) Проверка созданного нового пользователя rvs2
if grep -q "^rvs2" /etc/passwd; then
    echo "Пользователь rvs2 был успешно создан"
else
    echo "Не удалось создать пользователя rvs2"
fi

#11) Копируем из директории home/rvs/STUD в директорию home/rvs2 папки с содержимым stud_bash
sudo cp -r /home/rvs/STUD/stud_bash /home/rvs2/

#12) Проверяем наличие в директории home/rvs2 папки stud_bash
if [ -d /home/rvs2/stud_bash ]; then
  echo "Директория /home/rvs2/stud_bash существует"
else
  echo "Директория /home/rvs2/stud_bash не сущетсвует! Исправь скрипт"
fi
 
# 13) Создание резервной копии домашней директории с указанием даты и времени создания копии
DATE=$(date +%Y-%m-%d_%H-%M-%S)
sudo tar -czvf "backup_$DATE.tar.gz" /home/rvs2

# 14) Проверить, создался файл лога или нет и время его изменения

file_path="/home/rvs/STUD/stud_bash/log.txt"

if [ -e "$file_path" ]; then
    echo "Файл $file_path существует."
    modification_time=$(stat -c "%y" "$file_path")
    echo "Дата изменения файла: $modification_time"
else
    echo "Файл $file_path не существует."
fi

echo "Конец выполнения скрипта"
