#B083040012
D1={int:"i",float:"f",complex:"j"}
D2={"s":str,"L":list,"T":tuple,"S":set,"D":dict,"B":bool}

def doIfMatches(A,B):
    """This checks if the datatype for object A matches to the format string B
       (which means that it checks whether the last character of B indicates
       the datatype of object A).
       If they don't match, an error is printed and the program exits. 
         Note: there are better solutions than running "exit()", but we haven't
               learned those solutions yet, so you must just use exit(). (This
               is also true for all places below, where errors are detected.)
       If they do match, then:
        - The variable A is converted to a string.
        - If:
           - it is a dictionary, the {} symbols are converted to « » symbols.
           - it is a singleton tuple, the , is removed
           - it is an empty set, it becomes "{}"
        - Then print the string, according to the format of B (but B's last
          letter needs to first be converted to "s").                       """
    if((B[-1]=='s' and type(A)!=str) and (B[-1]=='i' and type(A)!=int) and (B[-1]=='f' and type(A)!=float) and (B[-1]=='j' and type(A)!=complex) and (B[-1]=='T' and type(A)!=tuple) and (B[-1]=='D' and type(A)!=dict) and (B[-1]=='S' and type(A)!=set) and (B[-1]=='L' and type(A)!=list) and (B[-1]=='B' and type(A)!=bool)):
        print("Error")
        exit()
    else:
        if(B[-1]=='i'): 
            print(B%(A),end="")

        elif(B[-1]=='f'):
            print(B%(A),end="")

        elif(B[-1]=='D'):
            B=B[:-1]+'s'
            A="«"+str(A)[1:-1]+"»"
            print(B%(A),end="")

        elif(B[-1]=='T' and (len(A)==0 or len(A)==1)):
            if(len(A)==1):
                B=B[:-1]+'s'
                A=str(A)[0:-2] + ")"
                print(B%(A),end="")
            elif(len(A)==0):
                B=B[:-1]+'s'
                A=str(A)
                print(B%(A),end="")


        elif(B[-1]=="S" and len(A)==0):
            print("{}",end="")

        elif(B[-1]=='j'):
            B=B[:-1]+'s'
            print(B%(int(A.real)),end="")
            print(B%(int(A.imag)),end="")
            print("j",end="")
                
        elif(B[-1]=='s'):
           print(B%(A),end="")

        else:
            B=B[:-1]+'s'
            A=str(A)
            #print(B)
            print(B%(A),end="")

def putfORi(S): return S[:-1]+((("."in S) and "f") or "i")

def handleNumbers(A,B):
    """This receives a number A and a format string B. The format string is 
       known to end in either "i", "f", or "j".
       If B ends in a "j" then:
        - The format string B is updated by calling putfORi(B)
        - The real part of A is printed by the format of B, but only if either:
           1)it is nonzero or 2)the string B has a "+" in it.
        - The imaginary part always prints. It will have a "+" or "-" in front 
          of it if the real part was printed; otherwise it will only have a "-"
           if it is negative. The imaginary part is always followed by a "j".
       If B ends in "i" or "f" then A is simply printed according to the format
       rule of B.                                                           """
    if(B[-1]=="j"):
        B=putfORi(B)
        if(B[-1]=="i"):
            if(A.real!=0 or B[1]=='+'):
                if(B[1]=="+"):
                    B="%"+B[2:]
                print(B%(int(A.real)),end='')
            if(A.imag>1 or A.real!=0):
                print("+",end="")
            print(B%(int(A.imag)),end='')
            print("j",end="")
        if(B[-1]=="f"):
            if(A.real!=0 or B[1]=='+'):
                if(B[1]=="+"):
                    B="%"+B[2:]
                print(B%(A.real),end='')
            if(A.imag>1 or A.real!=0):
                print("+",end="")
            print(B%(A.imag),end='')
            print("j",end="")
    else:
        print(B%(A),end="")
def fprint(sfs,vla,skv=[0]):
    """This receives a single format string, a variable-length argument, and a
       special keyword-only variable with the default value of a singleton list
       holding the number 0.
       -In saying "a single format string" we mean that the string begins with 
        a "%" and ends with a letter, with no letters or "%" in the middle.
          (But there are two special format strings: "*" and "?". 
	       A "*" indicates that a new printf() has begun, so that the counter needs 
           to reset to 0.
           A "?" indicates that this printf() has finished, so we need to check
           for unmatched extra objects in the provided list.)
       -As for the variable-length argument, it holds all of the arguments you
        give to printf(), beyond the first argument, which is a format string.
       -What is the special variable? In slides 76-90 of Lecture 6, we learned
        that mutable default types persist between calls to a function. So the
        value of 0 in this list can be update to 1, 2, 3, etc. and that change
        will persist.
        Thus, we can look into this value to find the index in the variable-
        length argument tuple.

        Now for the behavior:
        - If the format string is finished (ie, you receive a "?"), but the
          argument list is not completed (ie, the counter held in the special
          variable has not reached to the end of the variable-length argument
          tuple), then you print an error message and then exit().
        - If the argument list is finished, but there is a new format string,
          print an error message and then exit().
        - Copy the next value in the variable-length tuple to the name "me". 
        - If the format string ends in "a" and if the variable named "me" 
          holds a number, then convert into a string. Note: you must use the
          dictionary defined on Line #1 to do this. 
        - If the format string ends in "a" then use the dictionary defined on 
          Line #2 to replace the "a" with the appropriate letter for the 
          datatype of the variable "me". Note that if "me" had been a number, 
          it would by now be a string.
        - If the datatype of the value stored in "me" is a number, then call
          handleNumbers(). Otherwise, call doIfMatches().                   """
    if(sfs=="*"):
        skv[0]=0
        return
    if(sfs=="?"):
        if(skv[0]!=len(vla)):
            print("Error")
            exit()
        else:
            return
    if(vla==()):
        print("Error")
        exit()
    me=vla[skv[0]]
    if(sfs[-1]=='a' and (type(me)==int or type(me)==float or type(me)==complex)):
        me=str(me)
        sfs=sfs[:-1]+'s'
    elif(sfs[-1]=='a'):
        if(type(me)==str):
            sfs=sfs[:-1]+'s'
        elif(type(me)==list):
            sfs=sfs[:-1]+'L'
        elif(type(me)==tuple):
            sfs=sfs[:-1]+'T'
        elif(type(me)==set):
            sfs=sfs[:-1]+'S'
        elif(type(me)==dict):
            sfs=sfs[:-1]+'D'
        elif(type(me)==bool):
            sfs=sfs[:-1]+'B'
    if(type(me)==int or type(me)==float or type(me)==complex):
        handleNumbers(me,sfs)
    else:
        doIfMatches(me,sfs)
    skv[0]+=1



def printf(*argu):
    """This implements the printf() function. It receives a variable number of
       arguments (including perhaps zero arguments, indicating to do nothing).

       The behavior is to walk through the format string passed in as the first
       argument, looking for "%" symbols. When one is found, we keep looking
       to find the next letter. The characters in between are a single format
       string. We can then call fprint() to handle the printing of this current
       argument.
       There are some considerations:
         - "%%" is not a format string, but just the way to print a "%".
         - In calling fprint(), it needs to be initialized first, by passing in
           a "*". This is because we may do more than one printf().
         - When finished, we need to check that we didn't finish with an
	   unmatched %.
         - When finished, we need to call fprint() again with a "?" to ensure
           that there were no extra arguments.                              """
    if(argu==()):
        print("",end='')
        return
    i=0
    k=0
    expr=argu[0]
    value=argu[1:]
    if(type(expr)!=str):
        print("Error")
        exit()
    if(("%" not in expr) and value!=()):
        print("Error")
        exit()
    while(i<len(expr)):
        #print(len(expr))
        if(expr[i]=="%"):
            if(len(expr)==1):
                print("Error")
                exit()
            if(expr[i+1]=="%"):
                print("%",end="")
                i=k=i+2
            else:
                while(not(expr[k]>"A" and expr[k]<"Z") and not(expr[k]>="a" and expr[k]<"z")):
                    k+=1
                    if(k>len(expr)):
                        break
                if(k>len(expr) or (expr[k]!='a' and expr[k]!='i' and expr[k]!='f' and expr[k]!='j' and expr[k]!='s' and expr[k]!='L' and expr[k]!='S' and expr[k]!='T' and expr[k]!='D' and expr[k]!='B')):
                    print("Error")
                    exit()
                i,k=k,i
                fprint(expr[k:i+1],value)
                i=k=i+1
        elif(expr[i]=="\t"):
            print(" ",end="")
            i=k=i+1
        elif(expr[i]=="\\"):
            print("\\",end="")
            i=k=i+1
        elif(expr[i]=="\n"):
            print("")
            i=k=i+1
        else:
            while(expr[i]!="%" and expr[i]!="\\" and expr[i]!="\t" and expr[i]!="\n"):
                i+=1
            print(expr[k:i],end="")
            k=i
    fprint("?",value)
    fprint("*",(),)

if __name__ == "__main__":
    from testNums import *
    from testTypes import *
    from testAny import *
    from testSpecials import *
    testNums()
    testTypes()
    testAny()
    testSpecials()