import numpy as np

def Mesh(length,width):
	l = np.linspace(0, length, num=length, dtype=np.int32)
	w = np.linspace(0, width, num=width, dtype=np.int32)


	m = np.meshgrid(l, w)
	print("Shape : ", m.shape)
	print(m)

def Mesh2():
	x = np.linspace(0, 5, 5, dtype=np.int32)
	y = np.linspace(0, 5, 5, dtype=np.int32)
	# full coordinate arrays
	xx, yy = np.meshgrid(x, y)

	print(yy)
	print(xx)

	#zipped = zip(xx, yy)
	#for cord in zipped:
	#	print(cord)

if __name__ == "__main__":

	Mesh2()

