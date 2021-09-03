from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .models import CronMon
from django.views.generic import View
from . import TimeWrapper


def control_panel(request):
	cron_fields = list(CronMon.objects.all().values())
	context = {'title':'RPA | Control Panel', 'values':cron_fields}
	return render(request, 'control_panel.html', context=context)


def shortjob(request):
	time_wrapper = TimeWrapper.TimeWrapper()
	time_wrapper.seconds(3)
	return JsonResponse({"response": 100}, safe=False)

def cronjob(request):
	toggle = request.headers.get('Authorization')
	if toggle == 'true':
		cron_obj = CronMon.objects.get(name='cronjob')
		cron_obj.status = True
		cron_obj.save()

	else:
		cron_obj = CronMon.objects.get(name='cronjob')
		cron_obj.status = False
		cron_obj.save()

	data = list(CronMon.objects.filter(name='cronjob').values())
	try:
		time_wrapper = TimeWrapper.TimeWrapper()
		print("Job started")
		status = data[0]['status']
		while status:
			print(datetime.now().strftime("%H:%M:%S"))
			time_wrapper.seconds(seconds=10)
			status = list(CronMon.objects.filter(name = 'cronjob').values())
			status = status[0]['status']
		return JsonResponse({'status': status, "info": "Job finished"}, safe=False)
	except Exception as e:
		print(e)
		return JsonResponse({'error': str(e)}, safe=False)

def perday(request):
	toggle = request.headers.get('Authorization')
	if toggle == 'true':
		perday_obj = CronMon.objects.get(name='perday')
		perday_obj.status = True
		perday_obj.save()

	else:
		perday_obj = CronMon.objects.get(name='perday')
		perday_obj.status = False
		perday_obj.save()

	data = list(CronMon.objects.filter(name='perday').values())
	try:
		time_wrapper = TimeWrapper.TimeWrapper()
		print("Job started")
		status = list(CronMon.objects.filter(name = 'perday').values())
		status = status[0]['status']
		while status:
			today = datetime.now().strftime("%A")
			if today == "Friday":
				status = list(CronMon.objects.filter(name = 'perday').values())
				status = status[0]['status']
				print("Friday job started")
				time_wrapper.seconds(seconds=30)
				print("Friday job finished")
				time_wrapper.days(days=1)
		return JsonResponse({'status': status, "info": "PerDay Job finished"}, safe=False)
	except Exception as e:
		print(e)
		return JsonResponse({'error': str(e)}, safe=False)

def perdate(request):
	toggle = request.headers.get('Authorization')
	if toggle == 'true':
		perdate_obj = CronMon.objects.get(name='perdate')
		perdate_obj.status = True
		perdate_obj.save()

	else:
		perdate_obj = CronMon.objects.get(name='perdate')
		perdate_obj.status = False
		perdate_obj.save()

	data = list(CronMon.objects.filter(name='perdate').values())
	try:
		time_wrapper = TimeWrapper.TimeWrapper()
		print("Job started")
		status = list(CronMon.objects.filter(name = 'perdate').values())
		status = status[0]['status']
		while status:
			today = datetime.now().strftime("%d")
			if today == '14':
				status = list(CronMon.objects.filter(name = 'perdate').values())
				status = status[0]['status']
				print("14th job started")
				time_wrapper.seconds(seconds=30)
				print("14th job finished")
				time_wrapper.days(days=1)
		return JsonResponse({'status': status, "info": "PerDate Job finished"}, safe=False)
	except Exception as e:
		print(e)
		return JsonResponse({'error': str(e)}, safe=False)

def pertime(request):
	toggle = request.headers.get('Authorization')
	if toggle == 'true':
		pertime_obj = CronMon.objects.get(name='pertime')
		pertime_obj.status = True
		pertime_obj.save()

	else:
		pertime_obj = CronMon.objects.get(name='pertime')
		pertime_obj.status = False
		pertime_obj.save()

	data = list(CronMon.objects.filter(name='pertime').values())
	try:
		time_wrapper = TimeWrapper.TimeWrapper()
		print("Job started")
		status = list(CronMon.objects.filter(name = 'pertime').values())
		status = status[0]['status']
		while status:
			now = datetime.now().strftime("%H:%M")
			if now == "10:00":
				status = list(CronMon.objects.filter(name = 'pertime').values())
				status = status[0]['status']
				print("10:00AM job started")
				time_wrapper.seconds(seconds=30)
				print("10:00AM job finished")
				time_wrapper.days(days=1)
		return JsonResponse({'status': status, "info": "PerTime Job finished"}, safe=False)
	except Exception as e:
		print(e)
		return JsonResponse({'error': str(e)}, safe=False)