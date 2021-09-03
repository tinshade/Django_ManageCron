import time
class TimeWrapper:
	def seconds(self, seconds=0):
		time.sleep(seconds)
		return True
	def minutes(self, mins=0):
		time.sleep(mins*60)
		return True
	def hours(self, hours=0):
		time.sleep(hours*3600)
		return True
	def days(self, days=0):
		time.sleep(days*86400)
		return True