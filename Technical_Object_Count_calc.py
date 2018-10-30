import pandas as pd
import os
import openpyxl
oxl= openpyxl.load_workbook('component_data.xlsx')
sheet  = oxl['Ark1']  #Sheet1 in norwegian
exception_file= ''
data= pd.read_excel('component_data.xlsx',sheet_name= 'Ark1')
path = '<Folder path from where you can get your content folders>'
try:
	for count, folder in enumerate(data['Folder Name'], 2):
		comp_path = path+'/'+str(folder)
		for root, dirs, file in os.walk(comp_path, topdown=False):
			pkb_count=0
			sh_count=0
			sql_count=0
			fmb_count=0
			prog_count=0
			ldt_count=0
			xml_count=0
			class_count=0
			rdf_count=0
			zip_count=0
			doc_count=0
			total=0
			for files in file:
				#print(files)
				total=total+1
				exception_file= files
				if files.endswith('pkb') or files.endswith('pks'):
					pkb_count=pkb_count+1
				if files.endswith('sh'):
					sh_count=sh_count+1;
				if files.endswith('sql'):
					sql_count=sql_count+1
				if files.endswith('fmb'):
					fmb_count= fmb_count+1
				if files.endswith('prog'):
					prog_count= prog_count+1
				if files.endswith('ldt'):
					ldt_count= ldt_count+1
				if files.endswith('xml'):
					xml_count= xml_count+1
				if files.endswith('class'):
					class_count= class_count+1
				if files.endswith('rdf'):
					rdf_count= rdf_count+1
				if files.endswith('zip'):
					zip_count= zip_count+1
				if files.endswith('docx'):
					doc_count= doc_count+1
				sheet['G'+str(count)] = pkb_count
				sheet['H'+str(count)] = sql_count
				sheet['I'+str(count)] = fmb_count
				sheet['J'+str(count)] = rdf_count
				sheet['K'+str(count)] = sh_count
				sheet['L'+str(count)] = prog_count
				sheet['M'+str(count)] = ldt_count
				sheet['N'+str(count)] = xml_count
				sheet['O'+str(count)] = zip_count
				sheet['P'+str(count)] = doc_count
				sheet['Q'+str(count)] = total
	oxl.save('mod_comp_data.xlsx')
except:
	print('Inner Exception : '+exception_file)
	oxl.save('mod_comp_data.xlsx')