

import face_recognition
import h5py

def faceimg():

	import os
	import cv2
	per_fold=os.listdir('data/')
	per_dict={}
	b=per_fold[0]
	a='data/'+str(b)
	#r=cv2.imread(a)
	#cv2.imshow('hi',r)
	#cv2.waitKey(0)  
	  
	#closing all open windows  
	#cv2.destroyAllWindows() 
	print(a)
	print(per_fold[0])
	known_face_encodings = []
	known_face_names = []
	#a='data/'+str(b)+'/abhin.jpg'
	import json

	
	for i,person in enumerate(per_fold):
		b=per_fold[i]
		a1='data/'+str(b)+'/'
		a=os.listdir('data/'+str(b)+'/')
		a=a1+''.join(a)

		print(a)
		
		img_data = face_recognition.load_image_file(a)
		known_face_names.append(person)
		face_encoding = face_recognition.face_encodings(img_data)[0]
		known_face_encodings.append(face_encoding)
		print(known_face_names)
		print(known_face_encodings)
		
		
	
	json_string = json.dumps(known_face_names)
	print(json_string)
	with open('name.json', 'w') as f:
		json.dump(known_face_names, f)
	with h5py.File('model.h5', 'w') as hf:
		hf.create_dataset('person',  data=known_face_encodings)
				
	return known_face_names,known_face_encodings

faceimg()

