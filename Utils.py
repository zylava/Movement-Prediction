import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from Import import dataImport, dataImportAverage, dataImportFront, dataImportBack
from Analyze import getSpan, getLow, makeDict, getEach, findGreatest, avgPressure, findPeaks, numPeaks

def makeTup(span, greatest, avg, numPeaks):
	
	tup = zip(span, greatest, avg, numPeaks)

	return tup


def makeTarget(movement, length):
	target = [movement] * length
	return target


def makeData(tup, target):
	X = np.array(tup)
	Y = np.array(target)
	return (X, Y)


def findModel(X, Y):
	knn = KNeighborsClassifier()
	k_range = range(1, 31)
	param_grid = dict(n_neighbors = k_range)
	grid = GridSearchCV(knn, param_grid, cv = 10, scoring = "accuracy", n_jobs = -1)
	grid.fit(X,Y)
	grid_mean_scores = [result.mean_validation_score for result in grid.grid_scores_]
	print grid.best_score_
	print grid.best_params_
	print grid.best_estimator_
	return grid.best_estimator_

def predict(knn, X, Y, to_predict):
	print knn.predict(to_predict)


def makeTraining(person):
	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person +'WALK_L.csv')
    # # plot_avg(avg_data, "..\plots\small.png", xlim, ylim)
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_WALK_L = makeTup(span, greatest, avg, num_peaks)
	target_WALK_L = makeTarget('WALK', len(tup_WALK_L))

	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'WALK_R.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_WALK_R = makeTup(span, greatest, avg, num_peaks)
	target_WALK_R = makeTarget('WALK', len(tup_WALK_R))

	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'SLOWWALK_L.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_SLOWWALK_L = makeTup(span, greatest, avg, num_peaks)
	target_SLOWWALK_L = makeTarget('SLOWWALK', len(tup_SLOWWALK_L))

	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'SLOWWALK_R.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_SLOWWALK_R = makeTup(span, greatest, avg, num_peaks)
	target_SLOWWALK_R = makeTarget('SLOWWALK', len(tup_SLOWWALK_R))


	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'RUN_L.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_RUN_L = makeTup(span, greatest, avg, num_peaks)
	target_RUN_L = makeTarget('RUN', len(tup_RUN_L))

	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'RUN_R.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_RUN_R = makeTup(span, greatest, avg, num_peaks)
	target_RUN_R = makeTarget('RUN', len(tup_RUN_R))

	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'JUMP_L.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_JUMP_L = makeTup(span, greatest, avg, num_peaks)
	target_JUMP_L = makeTarget('JUMP', len(tup_JUMP_L))


	(avg_data, xlim, ylim) = dataImportAverage('..\S' + person + 'JUMP_R.csv')
	valley_list = getLow(avg_data)
	points = getEach(valley_list)
	peaks = findPeaks(avg_data)
	num_peaks = numPeaks(peaks, points)
	span = getSpan(points)
	xy = makeDict(avg_data)
	greatest = findGreatest(xy, points)
	avg = avgPressure(points, xy)
	tup_JUMP_R = makeTup(span, greatest, avg, num_peaks)
	target_JUMP_R = makeTarget('JUMP', len(tup_JUMP_R))

 	tup = tup_WALK_L[1:] + tup_WALK_R[1:] + tup_SLOWWALK_L[1:] + tup_SLOWWALK_R[1:] + tup_RUN_L[1:] + tup_RUN_R[1:] + tup_JUMP_L[1:] + tup_JUMP_R[1:]
	target = target_WALK_L[1:] + target_WALK_R[1:] + target_SLOWWALK_L[1:] + target_SLOWWALK_R[1:] + target_RUN_L[1:] + target_RUN_R[1:] + target_JUMP_L[1:] + target_JUMP_R[1:]

	return tup, target


