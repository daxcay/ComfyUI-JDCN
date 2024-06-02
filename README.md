
![Cover_banner](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/b08ac26e-119c-44ee-abe4-78aa04370c6f)

# ComfyUI-JDCN
ComfyUI-JDCN, Custom Utility Nodes for Artists, Designers and Animators.

Jerry Davos Custom Nodes for Saving Latents in Directory (BatchLatentSave) , Importing Latent from directory (BatchLatentLoadFromDir) , List to string, string to list, get any file list from directory which give filepath, filename, move any files from any directory to any other directory, VHS Video combine file mover, rebatch list of strings, batch image load from any dir, load image batch from any directory and other custom nodes.

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/962cefe6-73b1-47ec-9f28-f2c1de51855c)

Since Most of the nodes are working with path, so it’s Ram efficient as actually loading of files is not done initially. 


# 1.	JDCN_AnyFileList :

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/33e48d53-a1fa-4cd0-990f-1816ea20a991)


Load Paths of any files from inside ComfyUI from a folder

•	folder_Path: Input the folder directory of the files you want to load without quotes. Eg: F:\Temp

•	filter_by: Filter files by major category – Images, audios, videos, texts, tensors, folders

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/236e8f53-fd76-407b-ad46-aec6f1680053)

•	extension: Filter files by their file extensions: 
-	Images: jpg, jpeg, png, gif, bmp, tiff, ico, svg, webp, psd, ai, eps, indd, cdr, raw, cr2, nef, orf, sr2, pef, x3f, dng, raf, rw2, arw, mef, mrw, fff, srf, kdc, mos, rwl, dcr, erf, 3fr, srw, bay, nrw, ptx, cap, iiq, eip, rwz, r3d, qtk, dcs, rw1, rpp, fff, rwl, pef, xmp
-	Audio: mp3, wav, flac, aac, ogg, wma, m4a, ape, alac, aiff, mid, opus, amr, pcm, mp2, ac3, ra, au, mka, snd
-	Video: mp4, avi, mkv, mov, wmv, flv, webm, mpg, mpeg, m4v, 3gp, rmvb, divx, vob, ts, ogv, m2ts, mts, f4v, asf
-	Text: txt, doc, docx, xls, xlsx, ppt, pptx, pdf, rtf, html, htm, xml, json, csv, dat, ini, cfg, inf, log, md, sql, php, cpp, java, py, c, h, hpp, js, css, asp, aspx, jsp, jspx, xhtml, rss, atom, pl, cgi, nfo, diz, reg, key, sfv, cue, url, bat, sh, ps1, vbs, asm, bak, tmp, temp
-	Tensors: latent



Example You can have all files in one folder and can filter & Separately use them: 

![1_1](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/9d6fbb9b-9269-43ba-9638-4e7ba7a0ce98)

Filter Photos and Use:

![1_2](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/1c5ce668-2f39-42bb-8d61-2a0a740bcbf4)

Use Single Video Via AnyFileSelector Node:

![3](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/c4679b17-6c38-4ae2-ab7f-46d13b4b9f18)


Filter and Use Multiple Videos at Once:

![2](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/6127343a-fec1-42fb-87e1-9a7d2217dede)

Filter Latents and Use:

![4](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/44cf4141-40d2-490f-ac50-a716ebc72ee3)


Filter Text files, jsons and load them inside comfy:

![5](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/24aafc56-ba98-4ca1-80ca-b0af1db5e5e9)


# 2.	JDCN_AnyFileListHelper

You can sort sperate List externally with a helper node.  

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/182d7bf3-9d30-4882-8254-7ac45f627490)


 
•	Search – Input keywords to search for – one or many keywords separated with comma

- EG: portrait,girl
  
•	Filter_by and extension are same as AnyFileList Node

Example workflow: 

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/9f3fee55-2d10-4e3d-9183-7e8e6de87bf7)

A folder with 12 Items in mixed format – webp, gif, png, json, jpeg

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/1509be91-b28b-4cb5-b3d2-ea9fd6d80bf7)

 
One Main List is divided by different formats selected in Helper node or you can search for specific term as shown in purple node
 
![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/cc7b5569-71b5-430d-8ef1-61bccf6557fc)

Also, multiple keywords can be used to filter out files.


# 3.	JDCN_AnyFileListRandom

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/05e6a0b2-5436-4e35-a207-bb5d1a99ac2b)

AnyFileListRandom can be used to select elements at a random, fixed or incremental order. 

•	Batch_Size – Set the number of files selected per queue. 

# 4.	JDCN_AnyFileSelector

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/9fa3c45d-27dd-4ab1-9979-c5579f04ba3f)

It is used to select 1 element from the given input list

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/d53d4b89-c0a2-4480-a2bb-2d53e921d759)

# 5.	JDCN_BatchImageLoadFromList
 
![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/38724fe4-706e-4ea3-906d-7ef1256568f5)

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/997ffa6f-4843-4539-bf01-9865e87b5086)

Load images in any supported format


# 6.	JDCN_BatchSaveLatent

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/bf2357bc-2576-4e31-a3a0-3bf2ff5c2faf)

This Export latents into a folder, to save vae encoding time or use later. 



# 7.	JDCN_BatchLatentLoadFromDir

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/bb98557d-73b6-4971-9e04-63b6714c5b88)

•	Directory – Enter a folder location

•	Load_Cap – Number of Latents to load

•	Skip_Frame – Skip the first n images.

 ![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/2ca06e82-e7c7-47b8-b2b9-fe35a18b4e83)

You can load latents directly from a Specific directory

# 8.	JDCN_BatchLatentLoadFromList
   
 ![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/d18ab87d-2d25-44a9-80c9-7058f9db4529)

•	Index – Start index of the latents from the path list inputted.

•	BatchSize – Number of Latents to load.

•	BatchDirection – Direction for selection of latents from the list.


NOTE : Index works differently in this node, it is depended on BatchSize 
For Example: You have 4 elements in the inputted list. (a,b,c,d) 

Scene 1: 
Index = 1
BatchSize = 2

Output = a, b 


Scene 2: 
Index = 2
BatchSize = 2

Output = c, d


![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/c4dc2337-153e-4a60-8071-3340f6e28fd0)




# 9.	JDCN_FileMover

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/bb3e93d4-bae1-47b6-8f76-a5da2541c801)

A folder containing files

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/1a77b4b2-cd7a-4d16-8ecb-6a014ded5307)

Images, Json, Videos are sorted with helper node then moved to a new location via File Mover node.

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/05be8295-19b0-443e-b4f9-05c7d05476a9)

Output Result after queue.

# 10.	JDCN_ImageSaver

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/fafad74e-8572-4da7-989f-37a8e6f78fb2)

Saves images into an output directory
•	OpenOutputDirectory: When enabled will open the Output folder.  


# 11.	JDCN_ListToString and JDCN_ StringToList

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/165e8599-07a3-4027-9d8d-efe38031506c)

Convert list to one single multiline text and vice versa where ever needed.

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/a675b836-dd36-4209-b046-f14928d9723d)


# 12.	JDCN_ReBatch

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/f2d1a991-563f-4b79-a76b-46ae09148e63)

•	BatchSize – Number of Elements for a single output packet

•	TextList – False will give list a comma separated form, True will give in new line. 

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/06a1b9e1-38c5-4be0-bbcf-279012bd222a)

 
# 13.	JDCN_SplitString

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/245439b6-a3b8-4a97-b26d-c113268e14ca)

It Split the input String or list of strings from a given search term and give outputs – Suffix, Prefix and Found at location 

•	SearchFor – Enter character or word to search for a String

•	StartFrom – Begin Searching the string from front or rear.

•	Occurrence – Split the String from nth Occurrence of the search term from front or rear. 

•	IncludeSearchFor – Include the SearchFro Term in the Outputs - Suffix


Example Use cases: 
Separate Extentsions

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/53b4f577-31ce-4b61-9a5e-2cbeb834ab5f)



Separate File names and Paths

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/af8bcd01-ae07-40dd-8618-e9454507bb34)

Go Folder Up:  

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/9188a34b-ae72-4468-bf8f-64ccc341bbba)

# 14.	JDCN_TXTFileSaver

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/fd28e1a5-bd75-4411-861f-85d6a82bc0f9)

It Saves string or Text content into a file

•	Directory – Input a Folder location to Save the text file

•	Mode – How to Handle same named file – Merge, OverWrite, SaveNew, MergeAndSaveNew

It will create a new file if same named file does not exists 

# 15.	JDCN_VHSFileMover

![image](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/50db7d3e-2c0e-4654-b692-031ee2d72b47)


Use it with a VHS video combine node to move the rendered file to the output Location
•	OverwriteFile – It will overwrite the file if they have same file name.

__________________________________________________________________________________________________________________________________________

# Installation

1) Using `comfy-cli` (https://github.com/yoland68/comfy-cli)

   ```
   comfy node registry-install comfyui-jdcn
   ```

3) Automatic Method with [Comfy Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- Inside ComfyUI > Click Manager Button on Side.
- Click `Install Custom Node` and Search for JDCN and Install this node:

![Manager_Screenshot](https://github.com/daxcay/ComfyUI-JDCN/assets/152957217/e4ed1778-6f9b-4e34-b8a6-19521771c9f5)

- Restart ComfyUI and it should be good to go

3) Manual Method
- Go to your Comfyui > Custom Nodes folder
- Run CMD from folder path box or right click on empty area and click open in terminal.
- Copy and Paste this command `git clone https://github.com/daxcay/ComfyUI-JDCN.git`
- Then go inside ComfyUI-JDCN with cmd or open new.
- and type `pip install -r requirements.txt` to install the requirements.

__________________________________________________________________________________________________________________________________________

# CREDITS

◉ Daxton Caylor - ComfyUI Node Developer 
- Discord - daxtoncaylor
- Email - daxtoncaylor@gmail.com
- Discord server: https://discord.gg/Z44Zjpurjp
- Commission Status:  🟢 **Open** 🟢



◉ Jerry Davos - Graphic Design and Nodes Ideas 
- Discord - jerrydavos
- Email - davos.jerry+ContactGithub@gmail.com
- Comfyui Workflows and Animations:  [Link 1](https://www.patreon.com/jerrydavos)   &   [Link 2](https://openart.ai/workflows/profile/jerrydavos)
- Commission Status:  🟢 **Open** 🟢

- Discord Server : https://discord.gg/z9rgJyfPWJ

______________________________

# Support for JDCN ❤️

If you like to suppport us you can help us by 

Donation:
https://paypal.me/jerrydavos








