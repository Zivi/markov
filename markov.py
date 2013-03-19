#!/usr/bin/env python



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    import re #regular expressions, used to remove symbols
    new_text = re.sub(r'[^a-z ]', " ", corpus.lower())
    #new_text1 = new_text.strip()
    #set up the dictionary, split the words into individual strings
    new_list = new_text.split()
    

    #loop through the list of words
    #take word and the word after that and make it the markov_dict's keys
    #take word #3 and make it the value

    markov_dict = {}

    for index in range(len(new_list)-2):
        word1 = new_list[index]
        word2 = new_list[index + 1]
        word3 = new_list[index + 2]
        
        

        #check if at the end of the word list
        # if index == len(new_list) - 3:
            # break
        #set the key of the markov_dict to the first two items in the list
        mkey = word1 + " " + word2
        mkey = (word1, word2)
        #check if the key is not in the dictionary already, if it's not
        #add key
        value_list = []

        if mkey not in markov_dict:
            markov_dict[mkey] = [word3]
        else:
            markov_dict[mkey].append(word3)            
            # value_list.append(word3)
        # if word3 in markov_dict[mkey]:
            # markov_dict[mkey] = value_list.append(word3)  
        # print markov_dict
    return markov_dict


def make_text(markov_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #retrieve a random key from the markov_dict
    #from the key, retrieve a random value
    #print them together
    #probability_factor =  int(markov_dict[mkey][word3]) * markov_dict[mkey]
    import random #allows to select random elements of markov_dict
    random_phrase = []
    random_key = random.choice(markov_dict.keys())
    random_phrase.append(random_key[0])
    random_phrase.append(random_key[1])

    while len(random_phrase) < 25:
        key1 = random_phrase[-2]
        #print "Heres key1"
        #print key1
        key2 = random_phrase[-1]
        #print "Heres key2"
        #print key2
        new_key = key1, key2
        random_value = random.sample(markov_dict[new_key], 1)[0]
        #print "Heres random value"
        #print random_value
        random_phrase.append(random_value)
 
 
    
    print random_phrase[0] + " " + random_phrase[1] + " " + random_phrase[2] + " " +random_phrase[3] + " " + random_phrase[4] + " " + random_phrase[5] + " " + random_phrase[6] + " " + random_phrase[7] + " " + random_phrase[8] + " " + random_phrase[9] + " " + random_phrase[10] + random_phrase[11] + random_phrase[12] + " " + random_phrase[13] + " " + random_phrase[14] + " " + random_phrase[15] + " " + random_phrase[16] + " " + random_phrase[17] + " " + random_phrase[18] + " " + random_phrase[19] + " " + random_phrase[20] + " " + random_phrase[21] + " " + random_phrase[22] + " " + random_phrase[23] + " " + random_phrase[24]

def main():
    from sys import argv
    script, filename = argv

    # Change this to read input_text from a file
    f = open(filename)
    pre_text = f.read()
    f.close()

    chain_dict = make_chains(pre_text)
    #print chain_dict
    random_text = make_text(chain_dict)
    #print random_text



if __name__ == "__main__":
    main()


 
