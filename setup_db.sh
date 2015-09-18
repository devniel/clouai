#!/bin/bash
echo "Trying----------------------------- to synch"
python manage.py makemigrations --settings=settings.production
python manage.py migrate --settings=settings.production
#echo "Finish manage.py synchdb ----------------------------"
#echo "from authentication.models import User; User.objects.create_superuser('dnielfs@gmail.com','justh4ck', username='devniel')" | python manage.py shell --settings=settings.production
#echo "Finish creating super user ----------------------------"