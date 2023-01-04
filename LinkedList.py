#np=nullpointer, sp=startpointer,flp=freelistpointer,nnp=newwnodepointer,pnp=previousnodepointer,tnp=thisnodepointer,cnp=currentnodepointer,cp=current pointer,print (List[cp].data)

np = -1
 
class ListNode:

	def __init__(self): 
		self.data = " "
		self.Pointer = np 

def InitialiseList():
  List = [ListNode() for i in range (7)]
  sp = np
  flp = 0
  for Index in range (6):
    List[Index].Pointer=Index+1
  List[6].Pointer=np
  return(List,sp, flp)

def InsertNode (List, sp, flp,NewItem,Flag):
 if flp != np:
    nnp = flp
    List[nnp].data= NewItem
    flp = List[flp].Pointer
    pnp=np
    tnp = sp
    while tnp != np and List[tnp].data<NewItem:
     pnp= tnp
     tnp= List[tnp].Pointer
    if pnp == np:
     List[nnp].Pointer = sp
     sp = nnp
    else:
     List[nnp].Pointer = List[pnp].Pointer
     List[pnp].Pointer = nnp

 else:
   print("Sorry no space for more data. ")
   Flag=True
 print("Start Pointer: ", sp)
 return(List, sp, flp,Flag)

def FindNode (dataitem,sp,List):
  cnp = sp
  while cnp != np and List[cnp].data != dataitem:
   cnp = List[cnp].Pointer
  if cnp != np:
   return ("The item can be found at pointer: ",cnp)
  else:
   return ("Item is not within the List.")

def DeleteNode (Data,List,sp, flp):
  tnp = sp
  while tnp != np and List[tnp].data != Data:
   pnp = tnp
   tnp = List[tnp].Pointer
  if tnp != np:
   if tnp == sp:
     sp = List [sp].Pointer
   else:
      List[pnp].Pointer = List[tnp].Pointer
   List[tnp].Pointer = flp
   flp = tnp
  else: 
   print("Data does not exist within the List.")
  
  return (sp,flp,List)

def OutputAllNodes (List, sp):
  cp = sp
  if cp != np:
    while cp != np:
      
      print(List[cp].data,List[cp].Pointer)  
      cp = List[cp].Pointer
  else:
    print("The List is empty.")
    

def GetOption ():
  print ("Type the option you wish to choose ")
  print ("1: Insert data to list")
  print ("2: Search for data in the list.")
  print ("3: Delete a data from the list.")
  print ("4: Output all data in the list.")
  print ("5: Close the list")
  Choice = int(input("Your option: "))
  return (Choice)

List,sp, flp = InitialiseList()
Choice=GetOption()

for index in range (7):
  print(List[index].data,List[index].Pointer)

while Choice != 5 :
  if Choice == 1 :
    Flag = False
    while Flag != True:
      NewItem = input("Data to be inserted: ")
      List, sp, flp,Flag = InsertNode (List, sp, flp,NewItem,Flag)
      for index in range (7):
       print(List[index].data,List[index].Pointer)
  if Choice == 2:
    dataitem = input("Data to be searched here: ")
    cnp = FindNode (dataitem,sp,List)
    print (cnp)
  if Choice == 3:
    Data = input("Data to be deleted from list: ")
    sp,flp,List = DeleteNode (Data,List,sp, flp)
    for index in range (7):
      print(List[index].data,List[index].Pointer)
  if Choice == 4:
    OutputAllNodes (List, sp)
  Choice=GetOption()
