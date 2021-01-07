from os import system as sys
import numpy as np
from obs_ids import obs_id
from astropy.io import fits


## this script assumes that summed images already exists 
## and source and region files are generated and stored in 
## analysis/region_files
## script asks to whether run a common source and region file
## for different observations or to use different source
## and region files for all observations 

## making directories.....


#filter_used=str(input("Enter filter to be used [uuu | um2 | uvv | uw1 | uw2] ::"))

filters=np.asarray(["uuu","um2","uvv","uw1","uw2"])

temp=np.asarray(["analysis/"+f_name+"_appended.img" for f_name in filters])

np.savetxt("appended_image_file_list",temp, delimiter="",newline="\n", fmt="%s")


for f_name in filters:
	trig = fits.open("analysis/output_files/"+f_name+"/maghist.fits")
	trig_time = str(float((trig[0].header['HISTORY'][15]).split()[2]))
	#hdu = fits.open("analysis/"+f_name+"_appended.img")
	#tstart = hdu[0].data['TSTART']
	sys("uvotproduct infile=analysis/"+f_name+"_appended.img outfile=analysis/output_files/"+f_name+"/product_maghist.fits plotfile=analysis/output_files/"+f_name+"/lightcurve_product.gif srcreg=analysis/region_files/common/src.reg bkgreg=analysis/region_files/common/bg.reg batpos=NONE xrtpos=NONE uvotpos=NONE groundpos=NONE timezero="+trig_time+" clobber=yes reportfile=analysis/output_files/"+f_name+"/product_report.txt exclude=NONE")
	#print(trig_time)
	sys("cp -T analysis/output_files/"+f_name+"/lightcurve_product2.gif analysis/plots/"+f_name+"_light_curve_product.gif")
