# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from polls.models import Question ,Choice
from django.utils import timezone
import random

for q in range(0 ,11):
    question =Question()
    question.question_text ='qst_' +str(q)
    question.pub_date =timezone.now()
    question.save()
    for c in range(0 ,random.randint(1 ,10)):
        choice =Choice()
        choice.choice_text ='chi_' +str(q) +'_' +str(c)
        choice.question =question
        choice.votes =random.randint(3 ,8)
        choice.save()



#>>> from func.filldb import createphoto
#>>> createphoto()