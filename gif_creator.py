import numpy as np
import matplotlib.cm as cm
from array2gif import write_gif
for i in range():
	gif_array=np.load("gif_%d.npy"%(i))
	gif=gif_array[0,:,:,:,0]

	new_gif=np.ndarray([20,32,32,3])

	new_gif[:,:,:,0]=gif
	new_gif[:,:,:,1]=gif
	new_gif[:,:,:,2]=gif	

	write_gif(new_gif, 'gif_%d.gif'%(i), fps=50)
