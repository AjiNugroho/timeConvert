import sys
str_12 = sys.argv[1]
str_12 = str_12.replace(" ","")
str_12 = str_12.lower()

if len(sys.argv) != 2:
    print('Program membutuhkan 1 argument saja')
    sys.exit()
if len(str_12) != 10:
    print('Format jam salah, format jam HH:MM:SS AM/PM')
    sys.exit()
    
def convert_24(str_12): 

    # kalau belakangnya AM dan depan bukan 12, return asli saja

    if str_12[-2:] == "am" and str_12[:2] != "12":
        return str_12[:-2]
      
    # kalau belakang AM dan depannya 12, brarti tengah malam 
    elif str_12[-2:] == "am" and str_12[:2] == "12": 
        return "00" + str_12[2:-2] 
           
      
    # kalau belakang PM depan 12, berarti siang, return asli   
    elif str_12[-2:] == "pm" and str_12[:2] == "12": 
        return str_12[:-2] 
          
    else: #lainnya kalau PM, jam di tambah 12
          
        return str(int(str_12[:2]) + 12) + str_12[2:-2] 
  
print(convert_24(str_12)) 
