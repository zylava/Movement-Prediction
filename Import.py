'''
Created on Oct 10, 2016

@author: zylava
'''
import csv



def dataImport(file):

    all_data = []
    ylim = 0
    xlim = 0
    with open(file, 'r') as f:
        lines = f.readlines();

        for i, line in enumerate(lines):
            lines[i] = line.replace('\n','')

        indices = lines[0].split(',')
        for i in range (1, 100):
            elem = (indices[i], [])
            all_data.append(elem)


        for i, line in enumerate(lines):
            if(i == 0):
                continue
            elems = line.split(',')
            time = elems[0]
            del elems[0]
            for j, elem in enumerate(elems):
                if float(elem) > ylim:
                    ylim = float(elem)
                point = (time, elem)
                all_data[j - 1][1].append(point)

        xlim = float(time)

    return all_data, xlim, ylim

def dataImportAverage(file):
    avg_data = []
    ylim = 0
    with open (file, 'r') as f:
        lines = f.readlines()

        for i, line in  enumerate(lines):
            lines[i] = line.replace('\n','')

        for i, line in enumerate(lines):
            if (i == 0):
                continue
            elems = line.split(',')
            time = elems[0]
            del elems[0]
            sum = 0
            for j, elem in enumerate(elems):
                sum += float(elem)
            avg = sum / 99
            if avg > ylim:
                ylim = avg
            
            point = (time, avg)   
            avg_data.append(point)

        xlim = float(time)

    # print avg_data
    return avg_data, xlim, ylim

def dataImportBack(file):
    avg_data = []
    ylim = 0
    with open (file, 'r') as f:
        lines = f.readlines()

        for i, line in  enumerate(lines):
            lines[i] = line.replace('\n','')

        for i, line in enumerate(lines):
            if (i == 0):
                continue
            elems = line.split(',')
            time = elems[0]
            del elems[0]
            sum = 0
            for j, elem in reversed(list(enumerate(elems))):
                if (j < 90 ):
                    break;
                sum += float(elem)

            avg = sum / 99
            if avg > ylim:
                ylim = avg
            
            point = (time, avg)   
            avg_data.append(point)

        xlim = float(time)
        print xlim;

    # print avg_data
    return avg_data, xlim, ylim

def dataImportFront(file):
    avg_data = []
    ylim = 0
    with open (file, 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            lines[i] = line.replace('\n','')

        for i, line in enumerate(lines):
            if (i == 0):
                continue
            elems = line.split(',')
            time = elems[0]
            del elems[0]
            sum = 0
            for j, elem in enumerate(elems):
                if (j > 13):
                    break;
                sum += float(elem)

            avg = sum / 99
            if avg > ylim:
                ylim = avg
            
            point = (time, avg)   
            avg_data.append(point)

        xlim = float(time)
        print xlim;

    # print avg_data
    return avg_data, xlim, ylim
       

        
        

            
    
            