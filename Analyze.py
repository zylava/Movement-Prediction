import sys
from collections import OrderedDict
from enum import Enum
# Movement = Enum('WALK', 'JUMP', 'LEAN', 'RUN', 'STAND', 'SLOWWALK')

# get average pressure of each step
def avgPressure(points, xy):
	regularized = pointOhTwo(points)
	results = []
	
	for i in range(1, len(regularized)):
		sum = 0
		if regularized[i] is None or regularized[i - 1] is None:
			results.append(0)
			continue
		start = xy.keys().index(regularized[i - 1])
		end = xy.keys().index(regularized[i])
		for i in range(start, end):
			sum += xy.values()[i]
		results.append(sum / (end - start))

	return results

# makes points of minima a multiple of 0.02, 
#so that they could be used as dictionary keys
def pointOhTwo(points):
	regularized = []
	for i in range (len(points)):
		if points[i] is None:
			regularized.append(0)
			continue
		parts = str(points[i]).split('.')
		integer = parts[0]
		decimal = int(parts[1])
		times = int(decimal / 2)
		decimal = str(2 * times)
		# print decimal
		# if len(decimal) == 1:
		# 	decimal = decimal + '0'
		if decimal[-1] == '0':
			decimal = decimal[:-1]
		if decimal == '0' or len(decimal) == 0:
			point = integer
		else:
			point = integer + "." + decimal
		regularized.append(point)

		# print point

	return regularized


# find maximum in each step
def findGreatest(xy, points):
	regularized = pointOhTwo(points)
	results = []
	
	for i in range(1, len(regularized)):
		max = 0
		if regularized[i] is None or regularized[i - 1] is None:
			results.append(0)
			continue
		start = xy.keys().index(regularized[i - 1])
		end = xy.keys().index(regularized[i])
		for i in range(start, end):
			if xy.values()[i] > max:
				max = xy.values()[i]
		results.append(max)
	return results

#make the dataset into a order dictionary for easy access
def makeDict(avg_data):
	xy = OrderedDict()
	for each in avg_data:
		xy[each[0]] = each[1]
	return xy

#get start of a low and ending of a low
def getLow (avg_data):
	valley_list = []
	points = []
	span = []
	counter = 0
	counter_back = 0
	tmp_loc = -1

	# finding big decline
	for i in range (1, len(avg_data)):
		tup = ()
		# print avg_data[i][1]
		if (avg_data[i][1] < avg_data[i-1][1]):
			counter += 1
			# print "in decline: " + str(counter)
			counter_back = 0
			tmp_loc = -1
		elif (avg_data[i][1] > avg_data[i-1][1]):
			counter_back += 1
			# print "in incline: " + str(counter_back)
			if (tmp_loc == -1):
				if avg_data[i-1][1] < 5:
					tmp_val = avg_data[i-1][1]
					tmp_loc = avg_data[i-1][0]
					counter_back = 0
			else:
				counter_back += 1
				if (counter_back > 8):
					if valley_list:
						if (len(valley_list[-1]) != 2):
							valley_list[-1] = valley_list[-1] + (tmp_loc,)
						if (len(valley_list[-1]) == 2):
							tup = tup + (avg_data[i-1][0],)
							valley_list.append(tup)
					tmp_loc = -1

			# found local minima
			if counter > 8 and avg_data[i-1][1] < 5:
				# print "HIT LOWEST at: " + str(avg_data[i-1][0])
				tup = tup + (avg_data[i-1][0],)
				valley_list.append(tup)

				counter = 0
			else:
				# print "counter resets"
				counter = 0

	# print valley_list

	for i, each in enumerate(valley_list):
		if len(each) == 1:
			valley_list.pop(i)

	return valley_list

#using start of a low and ending of a low, get midpoint to use as minima
def getEach(valley_list):
	points = []
	for each in valley_list:
		if len(each) == 2:
			point = (float(each[1]) + float(each[0]))/ 2
			points.append(point)
		else:
			points.append(float(each[0]))
	return points


#using minima, get the span of time of each step
def getSpan(points):
	span = []
	for i in range(1, len(points)):
		# if points[i] is None or points[i- 1] is None:
		# 	span.append(0)
		# 	continue
		span.append(points[i] - points[i-1])

	return span


def findPeaks(avg_data):
	peaks = []
	counter_back = 0
	
	# finding big decline
	for i in range (1, len(avg_data)):
		tup = ()
		if (avg_data[i][1] < avg_data[i-1][1]):
			if counter_back > 5:
			# and avg_data[i-1][1] > 30:
				# print "HIT HIGHEST at: " + str(avg_data[i-1][0])
				peaks.append(avg_data[i-1][0])

			counter_back = 0
		elif (avg_data[i][1] >= avg_data[i-1][1]):
			counter_back += 1
			# print "in incline: " + str(counter_back)
			# found local minima

	return peaks

def numPeaks(peaks, points):
	numPeaks = [0] * (len(points) - 1)
	start_pos = 1
	for peak in peaks:
		# print peak
		for i in range (start_pos, len(points)):
			if i == 0:
				continue
			if float(peak) < points[i]:
				# print "incrementing " + str(points[i])
				numPeaks[i - 1] += 1
				break
			if float(peak) > points[i]:
				# print str(peak) + " is bigger than " + str(points[i])
				start_pos = i + 1
	return numPeaks

