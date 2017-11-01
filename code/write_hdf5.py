#_*_encoding:utf-8_*_
#!/usr/bin/env python
import numpy as np
import h5py
'''
对数据进行归一化等预处理，写入hdf5数据,运行后生成3个文件:
mine.h5:包含全部1599个数据
train.h5：包含训练集的1000个数据
test.h5：包含测试集的599个数据
'''


a=np.loadtxt('raw data/data.txt')


tmpA=np.zeros((1599,8))
tmpA[:,0:4]=a[:,0:4]
tmpA[:,4:8]=a[:,5:9]
normA=np.zeros(np.shape(tmpA))

minVals=tmpA.min(0)
maxVals=tmpA.max(0)
ranges=maxVals-minVals
m=tmpA.shape[0]
normA=tmpA-np.tile(minVals,(m,1))
normA=normA/np.tile(ranges,(m,1))

normA=normA.reshape(1599,1,8,1)
a=a.reshape(1599,1,9,1)
b=np.loadtxt('raw data/label.txt')

# b[:,0]=b[:,0]*500
# b[:,1]=b[:,1]*10
# b=b.reshape(1599,2)
label=b[:,0]
print label.shape
label=label.reshape(1599,1)
print label.shape
label_front=label[0:500]*0
print label_front.shape
label_end=np.zeros(1099)+1
print label_end.shape
label_end=label_end.reshape(1099,1)
print label_end.shape
# print label_end
label=np.vstack((label_front,label_end))
print label.shape


#f=h5py.File("train.h5","r")
#x=f["data"]
f2=h5py.File("data/mine.h5","w")
f2.create_dataset("data",data=normA,dtype='float32')
#f2.create_dataset("data",data=a,dtype='float32')
f2.create_dataset("label",data=b,dtype='float32')

trainData=normA[0:1000]
trainLabel=label[0:1000]

testData=normA[1000:]
testLabel=label[1000:]

f3=h5py.File("data/train.h5","w")
f3.create_dataset("data",data=trainData,dtype='float32')
f3.create_dataset("label",data=trainLabel,dtype='float32')

f4=h5py.File("data/test.h5","w")
f4.create_dataset("data",data=testData,dtype='float32')
f4.create_dataset("label",data=testLabel,dtype='float32')


