import re
import os


#This function identifies the Integrity Bug from the source code
def Integrity_Bug_Detector(file_path):
    
    with open(file_path, encoding="utf8") as file: #To open the verilog/SV file which encoded in UTF8
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            line = line.strip()
            if 'intg_err_o' in line and line.startswith('assign'): #To find the line with integrity error output
                lhs, rhs = line.split('=', 1)  # Split the line at to left hand side and right hand side
                lhs = lhs.strip()
                rhs = rhs.strip()
                if rhs.rfind('intg_err') == -1:
                    if rhs.startswith("1'b0") == -1:
                        print("Potential Bug Found!!")
                        print(f"File Location: "+str(file_path))
                        print(f"Line Number of the Bug: " +str(line_number))
                        print(f"Code Line: " +str(line))
                        print("____________________________________________________________________________")



            
            
 

#To analyze the verilog/SV files. This function will call the Integrity_Bug_Detector function for all the files available in the directory
def Scanner(directory):
    
    
    # Iterate through all Python files in the directory
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".sv") or file_name.endswith(".v"): #To find all the verilog/SV files in the directory
                
                file_path = os.path.join(root, file_name) #To ad the file name to the path
                Integrity_Bug_Detector(file_path)

                

    
                


#To get the Directory path of a Project
path = input(r"Enter the Project Path Here: ")
Scanner(path) #To Run the scanner





