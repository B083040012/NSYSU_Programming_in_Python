#B083040012
N={int:"i",float:"f",complex:"j"}	
M={"s":str,"L":list,"T":tuple,"S":set,"D":dict,"B":bytes,"y":bytearray,"z":frozenset}
#!!!!!!!%B represent both Booleans and Bytes
class FormattedString():
    """A formattedString object can be printed, accessed, updated, or 
       equality-compared."""
    def __init__(self,fstr,*args):
        """This makes an object holding the information of a formatted string.
        The behavior is to walk through the format string held in the first
        argument, looking for "%" symbols. When one is found, we keep looking
        to find the next letter. The characters in between are a single format 
        string. We can then test if the format is legal.
        If any format is wrong, or if any argument doesn't match the specified
        format type, or if the number of arguments doesn't match the number of
        format specifiers, then an error is generated. 
        Otherwise, the data type is created.                                """
            # Your code goes here. It must do the following steps:
            #  1. Create an instance attribute holding the format string, fstr
        self.hold=fstr
        self.position_in_fstr=0
            #  2. Make use of the __next__ method from below to iterate across
            #     that instance attribute.
            #  3. Whenever the next part is a format specifier:
            #     - Pass that specifier and the corresponding argument from 
            #       args into a private method that tests whether there are
            #       any problems (ie, if the format specifier is bad or if the
            #       corresponding argments type is not compatible with the
            #       specifier).
            #       - If there is a problem, raise an error (any type of error,
            #         because that is not important for this new assignment.
            #       - Otherwise, the private method simply returns. But note:
            #         since any problem will have raised an error, to return is
            #         the indication that there is no error.
            #       Note also that the implementation of this private method
            #       involves just reusing code from the previous homework
            #       solutions.
            #       - Use the __setitem__ method below to add the corresponding
            #       argument into some instance list attribute of arguments
        count=0
        self.arglist=[]
        while(self.position_in_fstr<len(fstr)):
            temp=next(self)
            if '%' not in temp:
                continue
            elif temp=="%%":
                continue
            else:
                if len(list(args))==0:raise SyntaxError("Argument not enough")
                self._FormattedString__private_test(temp,args[count])
                self.arglist.append(temp)
                self.__setitem__(count,args[count])
                count+=1
            #  4. If you run out of format specifiers before you run out of
            #     arguments (or vice versa), then raise an error (any error).
        if count!=len(args):
            raise SyntaxError("Extra value argument")
            
    def __getitem__(self,position):
        """This returns the argument at the indicated position. It is returned
        as a string created based on its corresponding format specifier."""
        ... # Your code goes here
        return self.arglist[position]

    def __setitem__(self,position,newValue):
        """This changes the argument stored at the indicated position, but only
        if newValue is compatible with the corresponding format specifier."""
        # Your code goes here
        if self.arglist[position][-1]=='a':
            if type(newValue) in N:
                newValue=str(newValue)
            elif type(newValue)!=bool:
                typpos=list(M.values()).index(type(newValue))
                self.arglist[position]=self.arglist[position][:-1]+list(M.keys())[typpos]
        if type(newValue) in N:
            if self.arglist[position][-1]=="j":
                end="j"
                self.arglist[position]=self.arglist[position][:-1]+("." in self.arglist[position] and "f" or "i")
                if '+' in self.arglist[position] or complex(newValue).real:
                    if '+' in self.arglist[position]:
                        self.arglist[position]="%"+self.arglist[position][2:]
                    self.arglist[position]=self.arglist[position]%(complex(newValue).real)+"+"+self.arglist[position]%(complex(newValue).imag)+'j'
                else:
                    self.arglist[position]=self.arglist[position]%(complex(newValue).imag)+'j'
            else:
                self.arglist[position]=self.arglist[position]%(newValue)
        else:
            S=str(newValue)
            if self.arglist[position][-1]=='D':S= "«"+S[1:-1]+"»"
            elif self.arglist[position][-1]=='S' and len(newValue)==0:S="{}"
            elif self.arglist[position][-1]=="T":
                if len(newValue)==0:S="()"
                elif len(newValue)==1:S=S[:-2]+")"
            elif self.arglist[position][-1]=="y":S="“"+S[12:-2]+"”"
            elif self.arglist[position][-1]=="z":S="⦓"+S[11:-2]+"⦔"
            elif self.arglist[position][-1]=="B":
                if S[0]=='b':S="‘"+S[2:-1]+"’"
                elif type(newValue)==bool:S=bool(newValue)
            self.arglist[position]=self.arglist[position][:-1]+'s'
            self.arglist[position]=self.arglist[position]%(S)

    def __iter__(self):
        return self

    def __next__(self):
        next_substr_of_fstr = self.__get_next_substr_of_fstr()
        if next_substr_of_fstr == "":
            self.position_in_fstr=0
            raise(StopIteration)
        self.position_in_fstr += len(str(next_substr_of_fstr))
        return next_substr_of_fstr

    def __get_next_substr_of_fstr(self):
        ... # Your code goes here.
        percent=False
        code=""
        for c in self.hold[self.position_in_fstr:]:
            if percent:
                code+=c
                if (code=="%%") or (c.isalpha()):
                    return code
                else:continue
            elif c=='%':
                code+=c
                percent=True
            else:
                return c
        if code=="%" or not(code[-1].isalpha()):raise SyntaxError("Illegal string")
        

        
    def __str__(self):
        """Returns a string which is the string that printf() generates."""
        ... # Your code goes here. But you must:
            #  1. Use the __next__ method to step through fstr
            #  2. Use the __getitem__ method to construct the portions of the
            #     string that you will be returning. (But note that not every
            #     step of the fstr iteration will be a format specifier -- some
            #     steps will return the text in between specifiers. Eg "A%iB%f"
            #     would yield 4 iterations.
        hold_iter=iter(self.hold)
        re=""
        co=0
        self.position_in_fstr=0
        while(1):
            try:
                temp=next(self)
                if temp=="%%":
                    re+='%'
                elif "%" in str(temp):
                    re+=self.__getitem__(co)
                    co+=1
                else:
                    re+=temp
            except:
                return re


    def __private_test(self,temp,argu):
        if type(argu)==None:raise SyntaxError("Error for no argument!")
        if temp[-1]=="a":
            return
        elif (type(argu) in N) and (temp[-1]!='i' and temp[-1]!='f' and temp[-1]!='j'):
            raise SyntaxError("Wrong format string for num!") 
        elif (type(argu)==bool) and temp[-1]!='B':raise SyntaxError
        elif (type(argu) not in N) and (type(argu)!=bool) and M[temp[-1]]!=type(argu):
            raise SyntaxError("Wrong format string for other type!")
        else:
            return

class printf(FormattedString):
    """NAME
      printf - format and print data

SYNOPSIS
      printf ([FORMAT [ARGUMENTS]] )

DESCRIPTION
      Print ARGUMENT(s) according to FORMAT string

      If no FORMAT string is given, do nothing.
      If no ARGUMENTS are given, then FORMAT must contain no format specifiers.


      FORMAT controls the output similar to the C language's printf. Compared
      to a C printf(), however, there are some differences in the format codes
      (eg, a %z is added, but there is no %g).

      Compared to a Python print statement, some datatypes print differently,
      because unicode symbols are used to indicate certain data types.

      The format specifier data types are either numeric or containers.
      - Numeric types:
          %B - (B)oolean type. Answer is "True" or "False". Format follows the
               string rules: printf("|%-6B|%+6B|",True,1==2) 🡆 |True  | False|
          %f - (f)loat type. Format options are the same as C printf. So, for
               example, printf("|%-+08.3f|",1.2)  🡆  |+1.200  |
          %i - (i)nteger type. Format options are the same as C printf. So, for
               example, printf("|%-+08i|",12)  🡆     |+1      |
          %j - complex type. No paretheses are put around complex numbers. 
               The format options will be described by cases:
               -Concerning the real part, it prints if it is nonzero, or if a +
                is used:  printf("|%j|%j|%+j|",1,1j,1j) 🡆 |1+0j|1j|0+1j|
               -Concerning the formating of the real and complex parts, they
                use the same format: printf("|%+03j|1+2j) 🡆 |001+002j|
               -Concerning the formating of the real and complex parts, they
                use the same format: printf("|%+03j|1+2j) 🡆 |001+002j|
               -Concerning whether to print as an integer or a float, that is
                determined by the presence of a '.' in the format:
                printf("|%3j|%4.1j|",1.1+2.2j,1.1+2.2j) 🡆 |  1+  2j| 1.1+ 2.2j|

      - Container types. These all follow the format rules of strings:
          %D - (D)ictionary type. It displays with surrounding symbols: «...».
          %L - (L)ist type. It displays with surrounding symbols: [...].
          %s - (s)tring type. It displays with no surrounding symbols.
          %S - (S)et type. It displays with surrounding symbols: {...}.
               Note: the empty set displays as {}.
          %T - (T)uple type. It displays with surrounding symbols: (...).
               Note: a singleton tuple doesn't print a comma after the element.
          %y - bytearra(y) type. It displays with surrounding symbols: “...”.
          %z - fro(z)enset type. It displays with surrounding symbols: ⦓...⦔.
          %B - (B)ytes type. It displays with surrounding symbols: ‘...’.
          %a - (a)ny type. Converts the argument to a string then uses string 
               rules to print. For example:
                 printf("|%-10a|%10a|",1,{1:2}) 🡆 |1         |    «1: 2»|

      There is also a special use of % to not indicate a format string:
       - "%%" - This not a format string, but just the way to print a "%".  """

    def __init__(self,fstr="",*args,noprint=False):
        """We want the formattedString base (ie, super) class to have access
        to the format string and the arguments. So we will need to use the
        super() function to invoke formattedString's __init__ from inside this
        current method (ie, inside of the __init__ for printf).
        If formattedString's __init__ doesn't crash, then the input must have
        been good.
        The next step is to print myself, unless noprint was passed in as true.
        Note: Since formattedString is a base class, and since the printf class
              doesn't have a __str__ function, the __str__ will be inherited,
              and so the print will work.  """
        # Your code goes here. (__init__ is the only method of printf.)
        super().__init__(fstr,*args)
        if noprint:return
        else:print(self)