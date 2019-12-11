import numpy as np
import matplotlib.pyplot as plt

import ZLFFI02

def AddData0(data0):
  data0[17,0] = 0
  data0[17,1] = 0
  data0[17,2] = 10.4079
  data0[17,3] = 10.4078
  data0[17,4] = 2.2017e-10
  data0[18,0] = 0
  data0[18,1] = 0
  data0[18,2] = 11.0201
  data0[18,3] = 11.02
  data0[18,4] = 3.20542e-10
  data0[19,0] = 0
  data0[19,1] = 0
  data0[19,2] = 11.6323
  data0[19,3] = 11.6322
  data0[19,4] = 4.04421e-10
  data0[20,0] = 0
  data0[20,1] = 0
  data0[20,2] = 12.2445
  data0[20,3] = 12.2444
  data0[20,4] = 4.76368e-10
  data0[21,0] = 0
  data0[21,1] = 0
  data0[21,2] = 12.8568
  data0[21,3] = 12.8567
  data0[21,4] = 5.36485e-10
  data0[22,0] = 0
  data0[22,1] = 0
  data0[22,2] = 13.469
  data0[22,3] = 13.4689
  data0[22,4] = 5.84188e-10
  data0[23,0] = 0
  data0[23,1] = 0
  data0[23,2] = 14.0812
  data0[23,3] = 14.0811
  data0[23,4] = 6.18809e-10
  data0[24,0] = 0
  data0[24,1] = 0
  data0[24,2] = 14.6934
  data0[24,3] = 14.6933
  data0[24,4] = 6.39795e-10
  data0[25,0] = 0
  data0[25,1] = 0
  data0[25,2] = 15.3057
  data0[25,3] = 15.3056
  data0[25,4] = 6.46722e-10
  data0[26,0] = 0
  data0[26,1] = 0
  data0[26,2] = 15.9179
  data0[26,3] = 15.9178
  data0[26,4] = 6.39475e-10
  data0[27,0] = 0
  data0[27,1] = 0
  data0[27,2] = 16.5301
  data0[27,3] = 16.53
  data0[27,4] = 6.1824e-10
  data0[28,0] = 0
  data0[28,1] = 0
  data0[28,2] = 17.1423
  data0[28,3] = 17.1422
  data0[28,4] = 5.83377e-10
  data0[29,0] = 0
  data0[29,1] = 0
  data0[29,2] = 17.7546
  data0[29,3] = 17.7545
  data0[29,4] = 5.35444e-10
  data0[30,0] = 0
  data0[30,1] = 0
  data0[30,2] = 18.3668
  data0[30,3] = 18.3667
  data0[30,4] = 4.7511e-10
  data0[31,0] = 0
  data0[31,1] = 0
  data0[31,2] = 18.979
  data0[31,3] = 18.9789
  data0[31,4] = 4.02952e-10
  data0[32,0] = 0
  data0[32,1] = 0
  data0[32,2] = 19.5912
  data0[32,3] = 19.5911
  data0[32,4] = 3.1884e-10
  data0[33,0] = 0
  data0[33,1] = 0
  data0[33,2] = 20.2034
  data0[33,3] = 20.2033
  data0[33,4] = 2.17927e-10
  done=True


  ZLFFI02.AddData0(data0)
