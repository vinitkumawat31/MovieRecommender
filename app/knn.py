import math
import copy 

def euclidean_distance(a,b,n):
	sum = 0;
	for i in range(0,n):
		sum+=(a[i]-b[i])*(a[i]-b[i])
	return math.sqrt(sum);

def knn(data_with_labels,k,p):
	data = copy.deepcopy(data_with_labels)
	for row in data:
		del row[0]
	dist_index = []
	for i in range(0,len(data)):
		distance = euclidean_distance(p,data[i],len(p))
		dist_index.append([distance,i])
	sorted_dist_index = sorted(dist_index)
	labels = []
	for i in range(0,k):
		label = data_with_labels[sorted_dist_index[i][1]][0]
		labels.append(label)
	return labels
