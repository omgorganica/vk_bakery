```
git clone https://github.com/omgorganica/vk_bakery.git
```

```
cd /vk_bakery
```
```
pip install -r req_win.txt для windows
или 
pip install -r req_nix.txt для *nix систем
```
```
touch .env с содержимым:
TOKEN = a0962a5bae809ab21ea5da7084fa470f262e8938744224dda7a2d0731a9000d1e2eb64f2725f9c718c277
COMMUNITY_ID = 204765770
VK_USER = your_vk_id
DB_USER = db_user
DB_PASSWORD = db_password
DB_NAME = db_name
HOST = localhost
```
```
python inserts.py для загрузки данных в БД
```

```
python server_manager.py
```