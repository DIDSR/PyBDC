# Quick Start Guide for PyBDC 1.0

1. To begin start by choosing a method: Sarno Koning, Sarno Incident Spectrum, or Hernandez Heterogeneous BCT
	
	1. Each method can be selected by selecting the radio button next to the method

		1. the default is Sarno Incident Spectrum

	2. Selecting the Sarno Koning BCT will lead to an output in the text box stating a description of Koning 
	   BCT apparatus

	3. Selecting the Hernandez Heterogeneous BCT method will lead to the text box on the bottom corner being
	   filled with the a description for each of the heterogeneous categories

2. After selecting a method, choose your parameters in the box next over
	
	1. Sample parameters include breast diameter, breast height, etc.
	
	2. Simply click on the downward arrow and choose the parameter of your choice

	3. You'll notice some parameters are deactivated and this is due to the method of your choice. Each method
	   uses different sets of parameters. As such, the parameters necessary for the method will remain active 
	   and those not necessary will remain inactive

3. After choosing parameters, enter your Air Kerma along with the input units and the desired output units. Air kerma is defined as the amount of energy deposited into the air when a photon passes through it. The number of projections should also
be added. This is defined as the number of individual X-ray measurements taken during the initial scan. 
	
	1. Simply enter your Air Kerma into the Air Kerma box and like before choose the input units in Air Kerma 
	   Units and output units via MGD Units by pressing the downward arrow

4. Depending on the method of your choice, you will have the option to input an incident spectrum and graph that 
   spectrum

	1. If you have chosen either Sarno Incident Spectrum or Hernandez Heterogeneous BCT, the option the input an 
	   incident spectrum will be available to you. 
		
		1. This is not optional; you must enter an incident spectrum for the method to work 
	
	2. Simply press the Input Incident Spectrum Button and a popup will appear prompting you to choose a file. 
	   Please select an appropriate text file following the format outlined in the complete user guide.
	
		1. Once an acceptable file has been chosen, a shortened file name will appear in the text box found on
		   the bottom left
	
	3. After inputting the file, the Graph Spectrum button will activate. You can then press the Graph Spectrum 
	   button which will display your incident spectrum on the graph

5. Once you are satisfied with all your inputs, you can press the Calculate Dose button found at the bottom left corner 
   next to the Clear Text button

	1. Pressing the Calculate Dose button will lead to an output in the text box of your mean glandular dose value 
	   and your chosen parameters. 
	
	2. The text will remain in the box unless you elect to clear the box. The box can be easily cleared by pressing 
	   the Clear Text button. Do note that your previous values will be cleared and cannot be retrieved.

6. [method_specific_inputs.toml](method_specific_inputs.toml) has method specific outputs given assumptions of homogenous or heterogenous composition
