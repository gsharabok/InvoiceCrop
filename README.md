# InvoiceCrop
The program takes in an image and crops the necessary tables. The table is set to Black and White, rotated, and denoised. \
Most image formats are supported, however, it is important to put the proper extension in the file variable. 

<img src="https://github.com/gsharabok/InvoiceCrop/blob/main/imgs/sample_image.jpg" />
<p align="center">
  <img width="250" height="250" src="https://github.com/gsharabok/InvoiceCrop/blob/main/imgs/down_arrow.png">
</p>

<p float="left">
  <img src="https://github.com/gsharabok/InvoiceCrop/blob/main/imgs/sample_image0_out.png" width="370" />
  <img src="https://github.com/gsharabok/InvoiceCrop/blob/main/imgs/sample_image1_out.png" width="370" /> 
</p>

---

<h2> To run: </h2> 
<p>	1. Ensure the necessary packages are installed. <br>
	2. Set the file variable to the path of your image (for Linux short path should be available, such as "./sample_image.jpg" or "sample_image.jpg") <br>
	3. Execute "python run.py" in the appropriate directory <br>
	4. The results are saved in the current folder with names in the format res(number).jpg <br>
	</p>
	
<h2> Points to note:  </h2>
<p>	1. If the image quality is high enough, the image will be contrasted and changed to pure black and white. This is the perfect scenario. <br>
	   If the quality is too bad, the words could become indistinguishable. <br>
	2. In most cases, there is only one table for the invoice so only res1.jpg will be created. Otherwise, multiple files will be created. <br>
	3. If a different output format is needed names inside cv2.imwrite() can be changed. <br>
	4. Tilted images will be corrected. However, this does not apply to tiny tilt, since the available tools are not this precise. <br>
	5. To install packages type "pip install -r requirements.txt"
	</p>
