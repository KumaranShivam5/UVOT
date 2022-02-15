# <span id="UVOT_SWIFT_data_analysis_automation_0"></span>UVOT SWIFT data analysis automation

-----

### <span id="Prequisites_3"></span>Prequisites

-----

  - download and install heasoft software
  - setup CALDB
  - download the necessary data to be anlysed
  - extract the downloaded archive in downloaded\_data folder inside
    working directory
  - create a folder “analysis” in working directory

to sum it up, all you need is to have these in your working directory,
rest of the directory structure will be created by the scripts

  - folders
      - downloaded\_data  
        (all the downloaded date extracted here)
      - analysis
          - region\_files  
            \-common  
            (containing source and region files created taking one of
            the images named as src.reg and bg.reg)
  - files
      - obs\_ids.py
      - uvotimsum\_script.py
      - uvotsource\_script.py
      - uvotmaghist\_script.py
      - 
**Good to go**

### <span id="DIRECTORY_STRUCTURE_27"></span>DIRECTORY STRUCTURE

-----

    |----downloaded_data
    |    |----<obs_id>
    |    |      |----auxil
    |    |      |----uvot
    |    |      |       |----image
    |    |      |       |       |----sw<obs_id><filter_name>_<type>.img.gz
    |    
    |----analysis
    |       |----output_files
    |       |      |----<filter_name>
    |       |       |       |----source_output_<obs_id><filter_name>.fits
    |       |       |       |----light_curve.gif
    |       |       |       |----maghist.fits
    |       |----region_files
    |       |       |----common
    |       |       |       |----src.reg
    |       |       |       |----bg.reg
    |       |       |----<filter_name>
    |       |       |       |----src.reg
    |       |       |       |----bg.reg
    |       |----summed_images
    |       |       |----<filter_name>
    |       |       |       |----sum_img_<obs_id><filter_name>.img
    |----obs_ids.py
    |----uvotimsum_script.py
    |----uvotmaghist_script.py
    |----uvotsource_script.py
    |----readme.md
    |----obs_id_list

### <span id="COMMAND_SEQUENCE_61"></span>COMMAND SEQUENCE

    $ python3 uvotimsum_script.py 

> this command will prompt to select a filter out of six filters
> availale  
> uvv | um2 | ubb | uw1 | uw2 | uuu

sums all the HDUs in downloaded .img files, excluding HDUs with
ASPCORR:NONE and stores in analysis/summed\_images/\<filter\_name\>  
uvotdetect \[chose any of the downloaded image for this, and

> create source and region files, and store in
> analysis/region\_files/common/src.reg and
> analysis/region\_files/common/bg.reg  
> this step is yet to be automated

    $ python3 uvotsource_script.py

> this command will prompt to select a filter out of six filters
> availale  
> uvv | um2 | ubb | uw1 | uw2 | uuu

optional, generate the source details and stores in
analysis/output\_files/\<filter\_name\>/source\_output\_\<obs\_id\>\<filter\_name\>.fits,
src and bg region must exist for this command to work  
(but in the corrent version , uvotsource\_script.py needs to be run
prior to running uvotmaghist to )

    $ python3 uvotmaghist_script.py

> this command will prompt to select a filter out of six filters
> availale  
> uvv | um2 | ubb | uw1 | uw2 | uuu

make sure src and reg files exist  
generate light\_curve corresponding to certain filter and stores in
analysis/outpt\_files/\<filter\_name\>/light\_curve.gif,
