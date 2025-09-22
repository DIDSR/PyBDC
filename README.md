# Python Breast Dosage Calculator: PyBDC
Python toolkit for calculating dosage for breast CT.
The following software enables accurate dose estimation for one or various breast exposures specifically for breast CT. This tool is a GUI software that can be used on Windows, Mac, and Linux operating systems. The mode is further explained below along with an overview of the methods, how to choose a method, the program inputs and buttons, the incident spectrum format, images of the GUI, and the accompanying data files.

Code execution
----------
Clone PyBDC repository.
```
git clone https://github.com/DIDSR/PyBDC.git
```

Run the following commands to install required dependencies.
```
apt-get -y install python3.11-tk
apt-get -y install pip
cd PyBDC
pip install -r requirements.txt
```

The required dependencies in [requirements.txt](requirements.txt).
```
customtkinter==5.2.2
matplotlib==3.8.0
numpy==1.26.0
pandas==1.3.4
```

Run PyBDC.
```
python3 PyBDC.py
```

PyBDC can also be run through its container available at https://huggingface.co/didsr/PyBDC-Container, or by executing the shell script [run_container.sh](run_container.sh).

User guide
----------
Please refer to the technical documentation https://pybdc.readthedocs.io/en/latest/

Disclaimer
----------
About the Catalog of Regulatory Science Tools
The enclosed tool is part of the Catalog of Regulatory Science Tools, which provides a peer-reviewed resource for stakeholders to use where standards and qualified Medical Device Development Tools (MDDTs) do not yet exist. These tools do not replace FDA-recognized standards or MDDTs. This catalog collates a variety of regulatory science tools that the FDA's Center for Devices and Radiological Health's (CDRH) Office of Science and Engineering Labs (OSEL) developed. These tools use the most innovative science to support medical device development and patient access to safe and effective medical devices. If you are considering using a tool from this catalog in your marketing submissions, note that these tools have not been qualified as Medical Device Development Tools and the FDA has not evaluated the suitability of these tools within any specific context of use. You may request feedback or meetings for medical device submissions as part of the Q-Submission Program.
For more information about the Catalog of Regulatory Science Tools, email RST_CDRH@fda.hhs.gov.

Tool Reference 
•	RST Reference Number: RST24MD17.01

•	Date of Publication: 09/19/2025

•	Recommended Citation: U.S. Food and Drug Administration. (2025). PyBDC: Python Breast Dosage Calculator (RST24MD17.01). https://cdrh-rst.fda.gov/pybdc-python-breast-dosage-calculator 

PyBDC Team: Harsha Marupudi, M.Eng., Joseph Manus B.S., Bahaa Ghammraoui, Ph.D. US Food and Drug Administration, Center for Devices and Radiological Health, Office of Science and Engineering Labs, Division of Imaging, Diagnostics, and Software Reliability.

References
----------
1. Sarno, A., Mettivier, G., Di Lillo, F., & Russo, P. (2017). A Monte Carlo study of monoenergetic and polyenergetic normalized glandular dose (DgN) coefficients in mammography. Physics in medicine and biology, 62(1), 306–325. https://doi.org/10.1088/1361-6560/62/1/306
2. Hernandez, A. M., Becker, A. E., & Boone, J. M. (2019). Updated breast CT dose coefficients (DgNCT ) using patient-derived breast shapes and heterogeneous fibroglandular distributions. Medical physics, 46(3), 1455–1466. https://doi.org/10.1002/mp.13391
3. Sechopoulos, I., Feng, S. S., & D'Orsi, C. J. (2010). Dosimetric characterization of a dedicated breast computed tomography clinical prototype. Medical physics, 37(8), 4110–4120. https://doi.org/10.1118/1.3457331
