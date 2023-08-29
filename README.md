## Описание
1 - из директории "infra" сбилдите образы командой:
```
 docker-compose up --build
```
2 - примените миграции:
```
docker compose exec backend python manage.py migrate  
```
3 - подгрузите данные из фистуры:
```
docker compose exec backend python manage.py load_data  
```
4 - запустить тесты можно командой:
```
docker compose exec backend python manage.py test
```
