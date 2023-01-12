from datetime import datetime as dt
import datetime
from django.shortcuts import render, HttpResponse
from event.models import Email

import time
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler

def job():
    time = dt.now()
    print("The current date and time is: "+ str(time))
    emails = Email.objects.all()
    for email in emails:
        print(email.scheduled_time)
  
        year = email.scheduled_time.strftime("%Y-%m-%d %H:%M")
        curr_dt = dt.today().strftime("%Y-%m-%d %H:%M")
        print("Curretn: "+curr_dt)

        print("Hell: "+year)

        if year == curr_dt:

            send_mail(email.subject, 
            email.message, 
            email.from_email, 
            [email.recipient_list], 
            fail_silently=False)

            email.sent = True
            email.save()


scheduler = BackgroundScheduler()
scheduler.add_job(job, trigger='interval', minutes=1)
# scheduler.add_job(job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])

scheduler.start()



# def myfunc():
#     emails = Email.objects.get(pk=1)
#     for email in emails:

#         send_mail(email.subject, 
#         email.message, 
#         email.from_email, 
#         [email.recipient_list], 
#         fail_silently=False)

#         print(email.scheduled_time + '\n\n\n\n')
#         email.sent = True
#         email.save()
#     time.sleep(60)


# job = scheduler.add_job(myfunc, 'interval', minutes=1)
# job.remove()

# while True:
#     emails = Email.objects.filter(sent=False,scheduled_time = dt.now())
#     for email in emails:

#         send_mail(email.subject, 
#         email.message, 
#         email.from_email, 
#         [email.recipient_list], 
#         fail_silently=False)

#         print(email.scheduled_time + '\n\n\n\n')
#         email.sent = True
#         email.save()
#     time.sleep(60)

# def home(request):
        
#     end_date = datetime(2023, 9, 9)  # End date for the countdown
#     remaining_time = end_date - datetime.now()  # Calculate the remaining time
#     return render(request, 'index.html', {'remaining_time': remaining_time})

def index(request):
    uuname = Email.objects.all()
    contex = {
        "uuname" : uuname,
    }
    return render(request, "index.html", contex)


def dates(request):
    uuname = Email.objects.all()
    contex = {
        "uuname" : uuname,
    }
    return render(request, "dates.html", contex)


# emails = Email.objects.all()
# for email in emails:
#     print(email.subject)

# while True:
#     send_mail(
#         'Subject here',
#         'Here is the message.',
#         'smartalarmclockiic@gmail.com',
#         ['smartalarmclockiic@gmail.com'],
#         fail_silently=False,
#     )
    