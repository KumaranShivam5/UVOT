from os import system as sys
import numpy as np
from obs_ids import obs_id




## making directories.....

#filter_used=str(input("Enter filter to be used [uuu | um2 | uvv | uvw1 | uvw2] ::"))
filters=np.asarray(["uuu","um2","uvv","uw1","uw2"])
for filter_used in filters:
	sys("rm -r  analysis/summed_images"+filter_used)
	sys("mkdir analysis/summed_images")
	#sys("mkdir summed_images")
	sys("mkdir analysis/summed_images/"+filter_used)


	##...running uvotimsum on all

	for ids in obs_id:
		to_sys="uvotimsum infile=downloaded_data/"+ids+"/uvot/image/sw"+ids+filter_used+"_sk.img.gz outfile=analysis/summed_images/"+filter_used+"/sum_img_"+ids+filter_used+".img expmap=no clobber=yes exclude=ASPCORR:NONE"
		sys(to_sys)

	#sys("uvotdetect infile=00010627079/uvot/image/sw00010627079um2_sk.img.gz[2] plot=yes outfile=new_dir/detect_00010627079.fits expfile=NONE clobber=yes threshold=3")



