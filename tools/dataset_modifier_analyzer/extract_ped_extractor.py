import pickle
import numpy

def extract_ped(datas,ped_cnt,data_cnt):
	result=[]
	for data in datas:
		ped_idx=numpy.where(data['annos']['gt_names']=='Pedestrian')
		if (len(ped_idx[0])>=ped_cnt):
			cur_data=data
			#cur_data['annos']['gt_bboxes_3d']=numpy.delete(cur_data['annos']['gt_bboxes_3d'],range(ped_idx[0][0]),axis=0)
			#cur_data['annos']['gt_names']=numpy.delete(cur_data['annos']['gt_names'],range(ped_idx[0][0]),axis=0)
			result.append(cur_data)
			if len(result)==data_cnt:
				break
	return result

file_name='data/rf2021/rf2021_infos_test_height_make'

with open(file_name+'.pkl','rb') as f:
	datas=pickle.load(f)

ped_cnt=10
data_cnt=100
ped_data=extract_ped(datas,ped_cnt,data_cnt)
print(ped_cnt, data_cnt, len(ped_data))


with open(file_name+'_ped_'+str(ped_cnt)+'.pkl','wb') as rf:
	pickle.dump(ped_data,rf,protocol=pickle.HIGHEST_PROTOCOL)
