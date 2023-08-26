## Описание
1 - из директории "infra" сбилдите образы командой: docker compose build
2 - поднимите контейнеры командой docker compose up
3 - примините миграции docker compose exec backend python manage.py migrate  
4 - подгрузите данные из фистуры docker compose exec backend python manage.py load_data  
