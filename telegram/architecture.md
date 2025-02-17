**Что где и как писать(желательно)?**

telegram/

- `/filters/`: Папка с кодом для фильтро(мб понадобятся)
    - `filters`: Файл для фильтров
- `/handlers/`: Папка для всех handlers
  - `admin_handlers.py`: handlers админа
  - `login_handlers.py`: handlers пользователя
  - `user_handlers.py`: handlers при авторизации
- `/keyboards/`:
  - `admin_keyboards.py`: keyboards админа
  - `login_keyboards.py`: keyboards пользователя(особенно для Сережи, который писал кейборды в хендлере)
  - `user_keyboards.py`: keyboards при авторизации
- `.env`: Здесь хранится токен
- `.env_example`: Пример, как должен выглядеть .env локально
- `config.py`: Для сбора токена из .env
- `main.py`: Основной файл запуска
- `architecture.md`: Описание архитектуры проекта
- `README_telegram.md`: Описание проекта и как с ним работать
