'''
Created on Oct 10, 2016

@author: zylava
'''
import matplotlib.pyplot as plt
import os
from math import ceil
import numpy as np

def plot(all_data, dir, xlim, ylim):
	if not os.path.exists(dir):
		os.makedirs(dir)

	ylim = ylim + 0.3 * ylim

	ylim = ceil(ylim)


	for i in range(0, 99):
		l = all_data[i][1]
		fig = plt.figure(figsize = (500, ylim/30))

		ax = fig.gca()

		ax.set_xticks(np.arange(0, xlim, xlim/1000))
		ax.set_yticks(np.arange(0, ylim, 10))

		plt.grid()

		plt.plot(*zip(*l))
		plt.ylim([0, ylim])
		fig.savefig(dir+'\\'+all_data[i][0]+'.png', dpi= fig.dpi)
		# plt.show()
		plt.close()

def plot_avg(avg_data, dir, xlim, ylim):
	# if not os.path.exists(dir):
	# 	os.makedirs(dir)

	ylim = ylim + 0.3 * ylim

	ylim = ceil(ylim)
	fig = plt.figure(figsize = (500, ylim))

	ax = fig.gca()

	ax.set_xticks(np.arange(0, xlim, xlim/1000))
	ax.set_yticks(np.arange(0, ylim, 1))

	plt.grid()

	plt.plot(*zip(*avg_data))
	plt.ylim([0, ylim])
	fig.savefig(dir, dpi = fig.dpi)
	# plt.show()
	plt.close()


def plot_avg_front_back(avg_data_front, avg_data_back, dir, xlim, ylim):
	# if not os.path.exists(dir):
	# 	os.makedirs(dir)

	ylim = ylim + 0.3 * ylim

	ylim = ceil(ylim)
	fig = plt.figure(figsize = (300, ylim))

	ax = fig.gca()

	ax.set_xticks(np.arange(0, xlim, xlim/1000))
	ax.set_yticks(np.arange(0, ylim, 10))

	plt.grid()

	plt.plot(*zip(*avg_data_front))
	plt.plot(*zip(*avg_data_back))
	plt.ylim([0, ylim])
	fig.savefig(dir, dpi = fig.dpi)
	# plt.show()
	plt.close()

