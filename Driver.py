'''
Created on Oct 10, 2016

@author: zylava
'''

from Plot import plot, plot_avg, plot_avg_front_back
from sklearn import datasets
from Import import dataImport, dataImportAverage, dataImportFront, dataImportBack
from Utils import makeData, findModel, predict, makeTraining

def driver():
    # iris = datasets.load_iris()
    # digits = datasets.load_digits()
    # print iris.data
    # print iris.target

    # (tup, target) = makeTraining('1')

    # (test, theoretical_result) = makeTraining('2')



    # (X, Y) = makeData(tup + test, target + theoretical_result)


    # knn = findModel(X, Y)


    # predict(knn, X, Y, test) 

    (avg_data, xlim, ylim) = dataImportAverage('..\S2LIMPLEFT_L.csv')

    plot_avg(avg_data, "..\plots\S2LIMPLEFT_L_AVG.png", xlim, ylim)
    (avg_data_front, xlim, ylim) = dataImportFront('..\S2LIMPLEFT_L.csv')
    (avg_data_back, xlim, ylim) = dataImportBack('..\S2LIMPLEFT_L.csv')
    plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S2LIMPLEFT_L_FRONT_BACK.png", xlim, ylim)



    # plot_avg(avg_data, "..\plots\S1WALK_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1WALK_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1WALK_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S1WALK_L_FRONT_BACK.png", xlim, ylim)

    # (avg_data, xlim, ylim) = dataImportAverage('..\S1STAND_L.csv')
    # plot_avg(avg_data, "..\plots\S1STAND_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1STAND_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1STAND_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S1STAND_L_FRONT_BACK.png", xlim, ylim)

    # (avg_data, xlim, ylim) = dataImportAverage('..\S1SLOWWALK_L.csv')
    # plot_avg(avg_data, "..\plots\S1SLOWWALK_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1SLOWWALK_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1SLOWWALK_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S1SLOWWALK_L_FRONT_BACK.png", xlim, ylim)

    # (avg_data, xlim, ylim) = dataImportAverage('..\S1RUN_L.csv')
    # plot_avg(avg_data, "..\plots\S1RUN_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1RUN_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1RUN_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S1RUN_L_FRONT_BACK.png", xlim, ylim)

    # (avg_data, xlim, ylim) = dataImportAverage('..\S1LEAN_L.csv')
    # plot_avg(avg_data, "..\plots\S1LEAN_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1LEAN_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1LEAN_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back,"..\plots\S1LEAN_L_FRONT_BACK.png", xlim, ylim)
    
    # (avg_data, xlim, ylim) = dataImportAverage('..\S1JUMP_L.csv')
    # plot_avg(avg_data, "..\plots\S1JUMP_L_AVG.png", xlim, ylim)
    # (avg_data_front, xlim, ylim) = dataImportFront('..\S1JUMP_L.csv')
    # (avg_data_back, xlim, ylim) = dataImportBack('..\S1JUMP_L.csv')
    # plot_avg_front_back(avg_data_front, avg_data_back, "..\plots\S1JUMP_L_FRONT_BACK.png", xlim, ylim)

   


    # (all_data, xlim, ylim) = dataImport('..\S1WALK_L.csv')
    # plot(all_data, "..\plots\S1WALK_L", xlim, ylim)
    # (all_data, xlim, ylim) = dataImport('..\S1STAND_L.csv')
    # plot(all_data, "..\plots\S1STAND_L", xlim, ylim)
    # (all_data, xlim, ylim) = dataImport('..\S1SLOWWALK_L.csv')
    # plot(all_data, "..\plots\S1SLOWWALK_L", xlim, ylim)
    # (all_data, xlim, ylim) = dataImport('..\S1RUN_L.csv')
    # plot(all_data, "..\plots\S1RUN_L", xlim, ylim)
    # (all_data, xlim, ylim) = dataImport('..\S1LEAN_L.csv')
    # plot(all_data, "..\plots\S1LEAN_L", xlim, ylim)
    # (all_data, xlim, ylim) = dataImport('..\S1JUMP_L.csv')
    # plot(all_data, "..\plots\S1JUMP_L", xlim, ylim)


if __name__ == '__main__':
    driver()