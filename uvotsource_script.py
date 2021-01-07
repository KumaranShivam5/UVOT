from os import system as sys
import numpy as np
from obs_ids import obs_id


## this script assumes that summed images already exists 
## and source and region files are generated and stored in 
## analysis/region_files
## script asks to whether run a common source and region file
## for different observations or to use different source
## and region files for all observations 

## making directories.....


#filter_used=str(input("Enter filter to be used [uuu | um2 | uvv | uvw1 | uvw2] ::"))

filters=np.asarray(["uuu","um2","uvv","uw1","uw2"])
for filter_used in filters:
	sys("rm -r  analysis/output_files/"+filter_used)
	sys("mkdir analysis/output_files")
	#sys("mkdir summed_images")
	sys("mkdir analysis/output_files/"+filter_used)


	##...running uvotimsum on all

	for ids in obs_id:
		to_sys="uvotsource image=analysis/summed_images/"+filter_used+"/sum_img_"+ids+filter_used+".img outfile=analysis/output_files/"+filter_used+"/source_output_"+ids+filter_used+".fits srcreg=analysis/region_files/common/src.reg bkgreg=analysis/region_files/common/bg.reg sigma=3 apercorr=CURVEOFGROWTH"
		sys(to_sys)

	#sys("uvotdetect infile=00010627079/uvot/image/sw00010627079um2_sk.img.gz[2] plot=yes outfile=new_dir/detect_00010627079.fits expfile=NONE clobber=yes threshold=3")



