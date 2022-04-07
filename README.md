# Playing with github actions
![tests](https://github.com/sav116/deploy_svc/actions/workflows/test_on_push.yaml/badge.svg)
## 0. Why
Пробуем создвть свой CI/CD пайплайн для домашнего проекта при помощи Python и GitHub Actions<br/>


## 1. Requirements
Для запуска этого проекта потребуется:
- VPS/VDS/VM с *nix ОС, куда будут деплоится контейнеры (проверено на Ubuntu Server 18.04)
- Белый IP адрес (проброшеный порт, иной способ получения веб хука)
- Python 3.8
- Docker
- git
## 2. Get Started
#####Установка серверной части на чистой Ubuntu Server 18.04
```shell script
sudo apt update
$ git clone https://github.com/sav116/deploy_svc.git
$ cd deploy_svc/ci_app/
$ sudo apt install python3-pip
$ sudo python3 setup.py install
$ sudo cp ../deploy_svc.service /etc/systemd/system/deploy_svc.service
# dont forget to add token in ci_example.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable deploy_svc.service
$ sudo systemctl start deploy_svc.service
```

Проверить то что веб сервер запустился и работает можно с помощью команд
```shell script
sudo systemctl status deploy_svc.service
```
или
```shell script
curl 0.0.0.0:5000
```
#####В Github аккаунте
Подключите Actions: https://github.com/features/actions<br/>
После этого вы можете писать свои действия в .github/workflows и смотреть как они выполняются во вкладке actions

## 3. Usage
При пуше нового кода в любую ветку будет запущена задача тестирования test_on_push, где будут проведены все тесты указанные в src/tests.py<br/>
При релизе (создании тэга) будет выполены действия из pub_on_release. А именно проход по всем тестам из src/tests.py. Если тесты будут пройдены успешно, то запустится процесс 
сборки докер образа, который будет отправлен в docker hub. Если пуш в регистри закончился успешно,
то будет отправлен вебхух на ранее установленный вебсервер, который и задеплоит наш контейнер

