Сервис рассылок
В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env
Запустить через команду python manage.py runserver
Кастомная команда для создания суперпользователя python manage.py csu
Необходимо запустить django-apscheduler командой python manage.py runapscheduler для работы в фоновом режиме. Останавливать django-apscheduler командой Ctrl+C в терминале
Разграничение ролей пользователей на уровне шаблонов и контроллеров:
Анонимный пользователь видит только главную страницу и может просматривать блоги
Зарегистрированный пользователь может просматривать, редактировать и удалять только свои рассылки, клиентов и письма
Менеджер может просматривать пользователей и рассылки, а также отключать пользователей и рассылки. При этом он не может редактировать или удалять пользовательские рассылки, клиентов или письма. Для того чтобы определить менеджера необходимо в админке создать группу 'manager' и присвоить следующие права
Can view настройка
Can change настройка
Can view user
Can change user
Далее назначить пользователю группу 'manager'
Для того чтобы определить роль контент-менеджера, зайдите в админку под паролем superuser'a и установите для него необходимые разрешения для создания, редактирования и удаления блога. Далее - заходить этим пользователем в админку.
Два вида кеширования(низкоуровневый для выборки статей блога в БД, на уровне контроллера - страница с конкретным блогом)
Логика работы системы:
После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
По ходу отправки сообщений должна собираться статистика по каждому сообщению для последующего формирования отчетов.
