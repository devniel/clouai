#!/bin/bash

#echo STARTINGD RUN.SH FOR STARTING DJANGO SERVER PORT IS $PORT
#
#echo ENVIRONMENT VAIRABLES IN RUN.SH
#printenv 

if [ -z "$VCAP_APP_PORT" ];
  then SERVER_PORT=5000;
  else SERVER_PORT="$VCAP_APP_PORT";
fi

echo [$0] port is------------------- $SERVER_PORT
python manage.py makemigrations --settings=settings.production
python manage.py migrate --settings=settings.production
#echo "from authentication.models import User; User.objects.create_superuser('dnielfs@gmail.com','justh4ck', username='devniel')" | python manage.py shell --settings=settings.production

echo [$0] Starting Django Server...
python manage.py runserver 0.0.0.0:$SERVER_PORT --noreload --settings=settings.production