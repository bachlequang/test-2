
import string
txt=open("count.txt", 'r')
txtf=txt.read()

#txtf='Python is a cool language but OCaml is even cooler since it is purely functional'
count ={}
a={}
#line=0


for words in txtf.split():
    words = string.lower(words)
    #for line in txtf:
    #if txtf.count(words) == 1:
    #if words  in txtf:
        #count[words]=txtf.count(words)
    count[words]=count.get(words,0)+1
#   {'is': 3, 'Python': 1, 'a': 1... }
                
        #if words in line:
           # a[words]=int(line)
        #count[line]=int(line)
        #while i < len(words):
          #  if words in txtf[i]:
            #        count[words]=txtf.count(words) - 1
            #i=i+1
    #else:
    #    count[words]-=1
                   # del count[words]
#if words in txtf:
  #                  count[words]=txtf.count(words)
    

                    
    
sortedchar_out_put = sorted(count.items())
for charoutput in sortedchar_out_put:
     print "%d %s" % (charoutput[1], charoutput[0])

txt.close()