import subprocess
from collections import Counter
import glob
import sys

def write_files(pdata,ndata,mimetype,datatype):
	print("For",mimetype,datatype,", no.of. positive files=",len(pdata),"no.o negative files=",len(ndata))
	for filename in pdata:
		filecontent = open(filename).read()
		bytes = dict([(chr(i),0) for i in range(256)])
		counter = Counter(filecontent)
		bytes.update(counter)
		l = zip(bytes.keys(),bytes.values())
		max_count = float(max(l,key=lambda x:x[1])[1])
		l = [(x[0],x[1]/max_count) for x in l]

		with open(mimetype+"_"+datatype+".txt","a") as f:
			f.write("\t".join([str(x[1]) for x in l])+"\t1\n")

	for filename in ndata:
		filecontent = open(filename).read()
		bytes = dict([(chr(i),0) for i in range(256)])
		counter = Counter(filecontent)
		bytes.update(counter)
		l = zip(bytes.keys(),bytes.values())
		max_count = float(max(l,key=lambda x:x[1])[1])
		l = [(x[0],x[1]/max_count) for x in l]

		with open(mimetype+"_"+datatype+".txt","a") as f:
			f.write("\t".join([str(x[1]) for x in l])+"\t0\n")

def make_matrix(pfolder,nfolder,mimetype):
	filenames = glob.glob(pfolder+"/*")
	n = len(filenames)
	p_training_files = filenames[:n/3]
	p_validation_files = filenames[n/3:2*n/3]
	p_test_files = filenames[2*n/3:]

	filenames = glob.glob(nfolder+"/*")
	n = len(filenames)
	n_training_files = filenames[:n/3]
	n_validation_files = filenames[n/3:2*n/3]
	n_test_files = filenames[2*n/3:]

	write_files(p_training_files,n_training_files,mimetype,"train")
	write_files(p_validation_files,n_validation_files,mimetype,"val")
	write_files(p_test_files,n_test_files,mimetype,"test")

def check_args(args):
	proceed = True
	pfolder = nfolder = mimetype = None
	try:
		mimetype = args[args.index('-t')+1]
		mimetype = mimetype.replace("/","-")

	except Exception as e:
		print("Please add the mimetype getting trained via the -t handler")
		proceed = False
	try:
		pfolder = args[args.index('-p')+1]
	except Exception as e:
		print("Please add folder for positive filetypes via the -p handler")
		proceed = False
	try:
		nfolder = args[args.index('-n')+1]
	except Exception as e:
		print("Please add folder for negative filetypes via the -n handler")
		proceed = False

	return proceed,pfolder,nfolder,mimetype

if __name__ == "__main__":
	proceed,pfolder,nfolder,mimetype = check_args(sys.argv)
	if proceed:
		#print("Mimetype chosen:",mimetype,"Positive folder",pfolder,"Negative folder",nfolder)
		make_matrix(pfolder,nfolder,mimetype)
		print("Dataset split complete...")
		cmd = ['./splitData.R',mimetype]	
		x=subprocess.call(cmd)
		print('Exit: Success with return', x)		
