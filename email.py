#Text file is must

def Read_Email_File():

    import collections

    fin = open('email.txt','r')

    a= fin.read()

    d={ }

    L=a.lower().split()

    for word in L:

        word = word.replace(".","")

        word = word.replace(",","")

        word = word.replace(":","")

        word = word.replace("\"","")

        word = word.replace("!","")

        word = word.replace("&","")

        word = word.replace("*","")

    for k in L:

        key=k

        if key not in d:

            count=L.count(key)

            d[key]=count

    n = int(input("How many most common words to print: "))

    print("\nOK. The {} most common words are as follows\n".format(n))

    word_counter = collections.Counter(d)

    for word, count in word_counter.most_common(n):

        print(word, ":", count)

    fin.close()

#Driver Code

def main():

    Read_Email_File()

main()