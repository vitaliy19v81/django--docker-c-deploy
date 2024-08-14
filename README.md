# django--docker-compose-deploy

# ssh ec2-user@ec2-54-144-87-242.compute-1.amazonaws.com


# Установка docker

# Прежде чем вы сможете установить Docker Engine, вам необходимо удалить все конфликтующие пакеты.
```Shell
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
# Перед первой установкой Docker Engine на новый хост-компьютер вам необходимо настроить репозиторий Docker.
```Shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
# Установите пакеты Docker.
```Shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# Убедитесь, что установка Docker Engine прошла успешно
```Shell
sudo docker run hello-world
```

# Установка docker compose
# Обновите индекс пакета и установите последнюю версию Docker Compose:
```Shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

# Убедитесь, что Docker Compose установлен правильно, проверив версию.
```Shell
docker compose version
```

# sudo apt install mc
# sudo apt install git

# создаем пользователя
# adduser new_user

# даем sudo права
```Shell
usermod -aG sudo new_user
exit
logout
```

# su root

# sudo usermod -aG docker new_user



# Создание ключа для частного репозитория
# ssh-keygen -t ed25519 -b 4096

# публичный ключ
# cat ~/.ssh/ed25519.pub

# Клонируем проект с репозитория
# git clone git@github.com.............deploiment.git 'заходим по ssh'

# ls

# cd django-docker-compose-deployment/

# cp .env.sample .env

# vi .env текстовый редактор
# wq выход

# docker compose -f docker-compose-deploy.yml up -d

# docker compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"

# docker compose -f docker-compose-deploy.yml logs