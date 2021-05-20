
class_names = ['aeroplane', 'bicycle' ,'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair',
               'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
print(len(class_names))
print(class_names)
res = {}
import numpy as np

for class_name in class_names:
    if class_name == 'aeroplane':
        ap = 0.601
    elif class_name == 'bicycle':
        ap = 0.654
    elif class_name == 'bird':
        ap = 0.501
    elif class_name == 'boat':
        ap = 0.299
    elif class_name == 'bottle':
        ap = 0.201
    elif class_name == 'bus':
        ap = 0.714
    elif class_name == 'car':
        ap = 0.655
    elif class_name == 'cat':
        ap = 0.699
    elif class_name == 'chair':
        ap = 0.215
    elif class_name == 'cow':
        ap = 0.544
    elif class_name == 'diningtable':
        ap = 0.557
    elif class_name == 'dog':
        ap = 0.632
    elif class_name == 'horse':
        ap = 0.666
    elif class_name == 'motorbike':
        ap = 0.678
    elif class_name == 'person':
        ap = 0.323
    elif class_name == 'pottedplant':
        ap = 0.266
    elif class_name == 'sheep':
        ap = 0.555
    elif class_name == 'sofa':
        ap = 0.511
    elif class_name == 'train':
        ap = 0.603
    elif class_name == 'tvmonitor':
        ap = 0.631

    res[class_name] = ap
np.save('1-voc2007_data.npy', res)

data = np.load('1-voc2007_data.npy', allow_pickle=True).item()
print(data['train'])

res2 = {}
for class_name in class_names:
    if class_name == 'aeroplane':
        ap = 0.701
    elif class_name == 'bicycle':
        ap = 0.665
    elif class_name == 'bird':
        ap = 0.602
    elif class_name == 'boat':
        ap = 0.187
    elif class_name == 'bottle':
        ap = 0.288
    elif class_name == 'bus':
        ap = 0.584
    elif class_name == 'car':
        ap = 0.531
    elif class_name == 'cat':
        ap = 0.623
    elif class_name == 'chair':
        ap = 0.245
    elif class_name == 'cow':
        ap = 0.603
    elif class_name == 'diningtable':
        ap = 0.233
    elif class_name == 'dog':
        ap = 0.611
    elif class_name == 'horse':
        ap = 0.637
    elif class_name == 'motorbike':
        ap = 0.723
    elif class_name == 'person':
        ap = 0.288
    elif class_name == 'pottedplant':
        ap = 0.275
    elif class_name == 'sheep':
        ap = 0.545
    elif class_name == 'sofa':
        ap = 0.335
    elif class_name == 'train':
        ap = 0.609
    elif class_name == 'tvmonitor':
        ap = 0.564

    res2[class_name] = ap
np.save('1-voc2012_data.npy', res2)

data = np.load('1-voc2012_data.npy', allow_pickle=True).item()
print(data['train'])


res3 = {}
for class_name in class_names:
    if class_name == 'aeroplane':
        ap = 0.801
    elif class_name == 'bicycle':
        ap = 0.801
    elif class_name == 'bird':
        ap = 0.692
    elif class_name == 'boat':
        ap = 0.537
    elif class_name == 'bottle':
        ap = 0.367
    elif class_name == 'bus':
        ap = 0.854
    elif class_name == 'car':
        ap = 0.891
    elif class_name == 'cat':
        ap = 0.803
    elif class_name == 'chair':
        ap = 0.375
    elif class_name == 'cow':
        ap = 0.883
    elif class_name == 'diningtable':
        ap = 0.403
    elif class_name == 'dog':
        ap = 0.611
    elif class_name == 'horse':
        ap = 0.677
    elif class_name == 'motorbike':
        ap = 0.883
    elif class_name == 'person':
        ap = 0.308
    elif class_name == 'pottedplant':
        ap = 0.565
    elif class_name == 'sheep':
        ap = 0.745
    elif class_name == 'sofa':
        ap = 0.605
    elif class_name == 'train':
        ap = 0.809
    elif class_name == 'tvmonitor':
        ap = 0.734

    res3[class_name] = ap
np.save('1-CorLoc_data.npy', res3)

data = np.load('1-CorLoc_data.npy', allow_pickle=True).item()
print(data['train'])


res4 = {}
for class_name in class_names:
    if class_name == 'aeroplane':
        ap = 0.601
    elif class_name == 'bicycle':
        ap = 0.654
    elif class_name == 'bird':
        ap = 0.401
    elif class_name == 'boat':
        ap = 0.219
    elif class_name == 'bottle':
        ap = 0.221
    elif class_name == 'bus':
        ap = 0.614
    elif class_name == 'car':
        ap = 0.675
    elif class_name == 'cat':
        ap = 0.499
    elif class_name == 'chair':
        ap = 0.285
    elif class_name == 'cow':
        ap = 0.444
    elif class_name == 'diningtable':
        ap = 0.357
    elif class_name == 'dog':
        ap = 0.432
    elif class_name == 'horse':
        ap = 0.466
    elif class_name == 'motorbike':
        ap = 0.678
    elif class_name == 'person':
        ap = 0.103
    elif class_name == 'pottedplant':
        ap = 0.266
    elif class_name == 'sheep':
        ap = 0.555
    elif class_name == 'sofa':
        ap = 0.511
    elif class_name == 'train':
        ap = 0.673
    elif class_name == 'tvmonitor':
        ap = 0.681

    res4[class_name] = ap
np.save('2-map_data.npy', res4)

data = np.load('2-map_data.npy', allow_pickle=True).item()
# print(len(data))
print(data['train'])



res5 = {}
for class_name in class_names:
    if class_name == 'aeroplane':
        ap = 0.821
    elif class_name == 'bicycle':
        ap = 0.824
    elif class_name == 'bird':
        ap = 0.705
    elif class_name == 'boat':
        ap = 0.549
    elif class_name == 'bottle':
        ap = 0.401
    elif class_name == 'bus':
        ap = 0.874
    elif class_name == 'car':
        ap = 0.905
    elif class_name == 'cat':
        ap = 0.659
    elif class_name == 'chair':
        ap = 0.405
    elif class_name == 'cow':
        ap = 0.714
    elif class_name == 'diningtable':
        ap = 0.457
    elif class_name == 'dog':
        ap = 0.532
    elif class_name == 'horse':
        ap = 0.686
    elif class_name == 'motorbike':
        ap = 0.908
    elif class_name == 'person':
        ap = 0.333
    elif class_name == 'pottedplant':
        ap = 0.606
    elif class_name == 'sheep':
        ap = 0.855
    elif class_name == 'sofa':
        ap = 0.551
    elif class_name == 'train':
        ap = 0.753
    elif class_name == 'tvmonitor':
        ap = 0.753

    res5[class_name] = ap
np.save('2-CorLoc_data.npy', res5)

data = np.load('2-CorLoc_data.npy', allow_pickle=True).item()
#print(len(data))
print(data['train'])
