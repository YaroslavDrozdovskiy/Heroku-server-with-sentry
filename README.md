# Heroku server with sentry

1. Скачайте исходный архив
2. Создайте локальное окружение командой **python -m venv venv**, затем (для пользователей Windows) пропишите **venv\Scripts\activate.bat**
3. Создайте репозиторий с файлами набором команд,находясь в папке проекта: **git init**; **git add .**  
**git commit -m "init"**
4. Установите необходимые зависимости **pip install -r requirements.txt** 
4. Инициализируйте heroku командой **heroku create**, затем деплоим проект **git push heroku master**; **heroku ps:scale web=1** и перейдите по ссылке
5. Установите переменные окружения и sentry: **heroku config:set APP_LOCATION=heroku** и  
**heroku config:set SENTRY= https://{key}@sentry.io/{project}**  
   где {key} и {project} у вас должны быть соответствующие вашему аккаунту данные.
5. Проверяем приложение добавляя пути **/success** и **/fail**
