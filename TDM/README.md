# Real Estate Market Model (REMM) 2.0  

## *Intro:*  
 
Every four years, the Wasatch Front’s two metropolitan planning organizations (MPOs), Wasatch Front Regional Council (WFRC) and Mountainland Association of Governments (MAG), collaborate to update a set of annual traffic analysis zone and small area population and employment projections for the Salt Lake City-West Valley City (WFRC), Ogden-Layton (WFRC), and Provo-Orem (MAG) urbanized areas.  

These projections are primarily developed for the purpose of informing long-range transportation infrastructure and services planning done as part of the four year Regional Transportation Plan (RTP) update cycle, as well as Utah’s Unified Transportation Plan, 2019-2050. Accordingly, the foundation for the most recent projections is largely data describing existing conditions for a 2015 base year, the first year of the latest RTP process. The projections are included in the official travel model, which are publicly released at the conclusion of the RTP process.  

WFRC and MAG have developed a spatial statistical model using the UrbanSim modeling platform to assist in producing these annual projections. This model is called the Real Estate Market Model, or REMM for short. REMM is used for the developable urban portions of Weber, Davis, Salt Lake, and Utah counties. While REMM models future development at the parcel level, the predicted demographic and employment count and distribution produced by REMM for each future year is used to inform WFRC and MAG’s forecasts at the Traffic Analysis Zone (TAZ) level. 

## *Installation*  
1) Install Arcgis Pro
	- [Google Drive Download](https://drive.google.com/file/d/1eBHkQBPSMhGBrUjBYc1RORtBpkqA4N97/view?usp=sharing)
	- Accept the default installion parameters

2) Setup Cloned Python Environment
	- Open Arcgis Pro, preferably as an administrator
	- Click Settings -> Python -> Manage Environments
	- Click Clone Default
	- Change the name to "arcgispro-py3-REMM", or another descriptive name
	- Record the file path where the environment was installed for later
	- Keep Arcgis Pro open

3) Install python libraries
	- Open the command prompt (Run as administrator)
	- navigate to the *Scripts* folder inside your cloned python environment. Hint: It's usually on the C: drive, but you can check in the arcgis pro environment manager screen. See the example command below. Note: you may have to change drives in command line first.
	- Example: cd C:\Users\jsmith\AppData\Local\ESRI\conda\envs\arcgispro-py3-remm\Scripts
	- Run the following commands:
		- pip install pandana
		- pip install urbansim-wfrc
		- pip install rtree

4) Clone or download (to .zip) the REMM environment from Github  
	- A) Git  
		- In file explorer, navigate to location where the REMM folder structure will live
		- Right-click in empty space, select *Git Bash Here*...
		- In the Git Terminal, clone the REMM repository using the command: git clone https://github.com/WFRCAnalytics/REMM2_For_Python3_Internal_Use
	- B) Download to zip  
		- Navigate to https://github.com/WFRCAnalytics/REMM2_For_Python3_Internal_Use in a web browser
		- Click the green *Code* button near the top and select *Download ZIP*
		- Save the zip file and extract the contents in the desired location

5) Extract Travel Demand Model from zipped folder
	- In the TDM folder, extract the contents of this zipped folder, keeping the base TDM folder structure intact

6) Launch REMM from IDE
	- Download and install IDE of choice (Note: it must be compatible with python 3.x and support switching of python interpreters.)
	- Some examples include: PyCharm, WingIDE, Spyder, PyScripter
	- In the environment settings of your IDE, switch default python interpreter to your cloned REMM python environment python.exe file from earlier
		- PyCharm: File -> Settings -> Project -> Project Interpreter -> Click gear icon -> Add -> System Interpreter -> Click ellipsis icon -> Locate python.exe
		- Spyder: Tools -> Preferences - Python interpreter -> Check use the following interpreter: -> Locate python.exe
	- Launch REMM by opening RunREMM.py or REMM_GUI.py and running the script


## *References:*  
http://www.urbansim.com  
Clay, Michael J. (submitted April 2018, under review) Infrastructure Alternatives Analysis with an Integrated Land Use and Transportation Forecasting Model. Journal of Urban, Planning and Transportation Research.  
