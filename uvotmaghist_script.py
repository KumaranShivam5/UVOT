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


#filter_used=str(input("Enter filter to be used [uuu | um2 | uvv | uw1 | uw2] ::"))



###------- copying 1st observation onto which every other files will be appended------ this appended file is appended.img -------####
#sys("cp -T analysis/summed_images/"+filter_used+"/sum_img_"+obs_id[20]+filter_used+".img analysis/summed_images/"+filter_used+"/appended.img")

#import numpy as np

###------- a new file with the ist of all files to be created to be used with fappend------
#file_names=[]
#for ids in obs_id:
#	to_write= "analysis/summed_images/"+filter_used+"/sum_img_"+ids+filter_used+".img"
#	file_names.append(to_write)
#file_names=np.asarray(file_names)
#file_names=np.reshape(file_names,(len(file_names),1))

#np.savetxt("analysis/summed_images/"+filter_used+"/file_name_list.lis",file_names,delimiter="",newline="\n",fmt="%s")
filters=np.asarray(["uuu","um2","uvv","uw1","uw2"])
for filter_used in filters:
	sys("ls analysis/summed_images/"+filter_used+"/ > temp_append_list.lis")
	image_name_list=np.asarray(np.loadtxt("temp_append_list.lis",dtype=str))
	temp=np.asarray(["analysis/summed_images/"+filter_used+"/"+image for image in image_name_list])
	np.savetxt("temp_append_list.lis",temp, delimiter="",newline="\n", fmt="%s")

	sys("cp -T analysis/summed_images/"+filter_used+"/"+image_name_list[0]+" analysis/"+filter_used+"_appended.img")

	###------appending files to new file appended.img----------
	#sys("mkdir analysis/summed_images/"+filter_used")

	#sys("fappend @analysis/summed_images/"+filter_used+"/file_name_list.lis analysis/summed_images/"+filter_used+"/appended.img")
	sys("fappend @temp_append_list.lis analysis/"+filter_used+"_appended.img")
	###---- running uvotmaghist on this appended image--- 
	sys("uvotmaghist infile=analysis/"+filter_used+"_appended.img outfile=analysis/output_files/"+filter_used+"/maghist.fits plotfile=analysis/output_files/"+filter_used+"/light_curve.gif exclude=NONE clobber=yes srcreg=analysis/region_files/common/src.reg bkgreg=analysis/region_files/common/bg.reg")

	sys("cp -T analysis/output_files/"+filter_used+"/light_curve.gif analysis/plots/"+filter_used+"_light_curve.gif")
	sys("rm temp_append_list.lis")


