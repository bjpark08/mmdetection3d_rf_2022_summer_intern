#data/rf2021/{dir_path}에 있는 relabeling dataset과 checkpoints에 있는 relabeling model들에 대해
#iteration 순서대로 validation 결과를 알려주는 함수

import os, sys

from tools.data_converter.create_gt_database import (
    GTDatabaseCreater, create_groundtruth_database)

os.environ['MKL_THREADING_LAYER'] = 'GNU'

iteration=5
data_root = 'data/kitti_relabeling/'
dir_path = 'relabeling_40/'

prefix = 'weak_kitti_40'

train1_file = prefix + '_infos_train1.pkl'
checkpoint1_file = 'checkpoints/iter1_0.pth'

train2_file = prefix + '_infos_train2.pkl'
checkpoint2_file = 'checkpoints/iter2_0.pth'

config = 'configs/centerpoint/centerpoint_02pillar_second_secfpn_4x8_cyclic_20e_weak_kitti.py'

######## 다른 파일로 돌릴 시 위의 부분들을 고쳐줄 것

cur_train1 = train1_file
cur_checkpoint1 = checkpoint1_file

cur_train2 = train2_file
cur_checkpoint2 = checkpoint2_file

for i in range(iteration):
    next_train1 = train1_file[:-4]+f'_{str(i+1)}.pkl'
    next_checkpoint1 = checkpoint1_file[:-6]+f'_{str(i+1)}.pth'

    next_train2 = train2_file[:-4]+f'_{str(i+1)}.pkl'
    next_checkpoint2 = checkpoint2_file[:-6]+f'_{str(i+1)}.pth'

    print(f"==============Validation Process of iteration {i+1}==============")
    relabel_valid1_message = \
        f"./tools/dist_test.sh {config} {cur_checkpoint1} 2 --eval mAP --show-dir results --validation-pkl {dir_path + cur_train2}"
    relabel_valid2_message = \
        f"./tools/dist_test.sh {config} {cur_checkpoint2} 2 --eval mAP --show-dir results --validation-pkl {dir_path + cur_train1}"

    print(relabel_valid1_message)
    os.system(relabel_valid1_message)
    print(relabel_valid2_message)
    os.system(relabel_valid2_message)

    cur_train1=next_train1
    cur_checkpoint1=next_checkpoint1

    cur_train2=next_train2
    cur_checkpoint2=next_checkpoint2