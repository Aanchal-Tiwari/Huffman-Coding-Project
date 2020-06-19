import heapq
import os


# Class of heap nodes
class heapNode:


    # Initialisation method
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

    # Overwrite less than for heap node
    def __lt__(self,other):
        return self.freq<other.freq

# Class with compressing and decompressing method
class huffmancoding:

    #initialisation method
    def __init__(self,path):
        self.path=path
        self.frequency={}
        self.heap=[]
        self.codes={}
        self.reverse_codes={}

    #method to get the freuency of characters
    def getfrequencies(self,text):
        for char in text:
            self.frequency[char]=self.frequency.get(char,0)+1

    #method to construct the heap with the help of frequency dictionary
    def constructheap(self):
        heapq.heapify(self.heap)
        for key in self.frequency:
            temp_node=heapNode(key,self.frequency[key])
            heapq.heappush(self.heap,temp_node)

    #method to make tree out of the heap
    def buildtree(self):
        while len(self.heap)>1:
            min1=heapq.heappop(self.heap)
            min2=heapq.heappop(self.heap)
            tempnode=heapNode(None,min1.freq+min2.freq)
            tempnode.left=min1
            tempnode.right=min2
            heapq.heappush(self.heap,tempnode)

    #method to generate codes
    def generatecodehelper(self,root,cur_code):
        if not root:
            return
        if root.char:
            self.codes[root.char]=cur_code
            self.reverse_codes[cur_code]=root.char
        self.generatecodehelper(root.left,cur_code+"0")
        self.generatecodehelper(root.right,cur_code+"1")

    #method t generate code and reverse code
    def generatecode(self):
        root=heapq.heappop(self.heap)
        self.generatecodehelper(root,"")

    #method to get encoded text out of simple text
    def encodedtext(self,input):
        result=""
        for element in input:
            result+=self.codes[element]
        return result

    #method to pad encoded text
    def getpaddedencodedtext(self,input):
        length=len(input)
        padding_required=8-length%8
        input=input+"0"*(padding_required)
        pad_info="{0:08b}".format(padding_required)
        input=pad_info+input
        return input

    #method to get byte form of encoded text
    def get_byte_encoded(self,padded_encoded_text):
        length=len(padded_encoded_text)
        if length%8!=0:
            print("Improper padding")
            exit(0)
        output=bytearray()
        for i in range(0,length,8):
            byte=padded_encoded_text[i:i+8]
            output.append(int(byte,2))
        return output

    #method to compress the file with path: self.path
    def compress(self):
        name,ext=os.path.splitext(self.path)
        output_path=name+"_compressed.bin"
        with open(self.path,"r+") as file , open(output_path,"wb") as output:
            text=file.read() #reading the file
            text=text.rstrip() # removing unwanted space
            self.getfrequencies(text) #constructig the frequency dictionary for character in text
            self.constructheap() #construct min heap on the basis of frequency of character in text 
            self.buildtree() #construct tree structure using the heap
            self.generatecode() #generate code of each of the characte
            encoded_text=self.encodedtext(text) #get encoded text out of simple tex
            padded_encoded_text=self.getpaddedencodedtext(encoded_text) #pad encoded text properly
            encoded_text_in_bits=self.get_byte_encoded(padded_encoded_text)
            output.write(bytes(encoded_text_in_bits))  
        print("Compressed")
        return output_path
    
    #output functions


    #method to remove padding
    def removepadding(self,input):
        pad_info=input[:8]
        input=input[8:]
        pad_info=int(pad_info,2)
        input=input[:-1*(pad_info)]
        return input

    #method to decode the text
    def decode(self,input):
        output=""
        cur_code=""
        for ele in input:
            cur_code+=ele
            if cur_code in self.reverse_codes:
                output+=self.reverse_codes[cur_code]
                cur_code=""
        return output

    def decompress(self,input):
        name,ext=os.path.splitext(self.path)
        output_path=name+"_decompressed"+".txt"
        with open(input,"rb") as file, open(output_path,"w") as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,"0")
                bit_string+=bits
                byte=file.read(1)
            bit_string=self.removepadding(bit_string)
            decoded_text=self.decode(bit_string)
            output.write(decoded_text)
        print("Decompressed")
        return output_path       
