import numpy as np
import cv2


capture = cv2.VideoCapture(0)

while (True):
	#untuk Menghasilkan Gambar Asli
	ret, frame = capture.read()
	#untuk Menghasilkan GrayScale
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #untuk Menghasilkan Gambar Negatif
	negatif = (255 - gray)
  #untuk Mengubah Brightness dari Gambar Asli
	changebrightness = (frame + 20)

  #untuk Menampilkan Gambar ke Webcam
	cv2.imshow('Gambar Asli',frame)
	cv2.imshow('Gray Scale',gray)
	cv2.imshow('Efek Negatif',negatif)
	cv2.imshow('Brightness',changebrightness)
	if cv2.waitKey(1) & 0xFF == ord('k'):
		break
		

cv2.destroyAllWindows()
capture.release()
