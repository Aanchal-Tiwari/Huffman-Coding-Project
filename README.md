# Huffman-Coding-Project----"Greedy Algorithm"
Huffman coding is an efficient method of compressing data without losing information. In computer science, information is encoded as bits—1's and 0's. Strings of bits encode the information that tells a computer which instructions to carry out. Video games, photographs, movies, and more are encoded as strings of bits in a computer. Computers execute billions of instructions per second, and a single video game can be billions of bits of data. It is easy to see why efficient and unambiguous information encoding is a topic of interest in computer science.
The process of finding or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes"

Let there be four characters a, b, c and d, and their corresponding variable length codes be 00, 01, 0 and 1. This coding leads to ambiguity because code assigned to c is the prefix of codes assigned to a and b. If the compressed bit stream is 0001, the de-compressed output may be “cccd” or “ccb” or “acd” or “ab”.

# There are mainly two major parts in Huffman Coding
1) Build a Huffman Tree from input characters.
2) Traverse the Huffman Tree and assign codes to characters.

# The Huffman Coding Algorithm

- Take a list of symbols and their probabilities.

- Select two symbols with the lowest probabilities (if multiple symbols have the same probability, select two arbitrarily).

- Create a binary tree out of these two symbols, labeling one branch​ with a "1" and the other with a "0". It doesn't matter which side you label 1 or 0 as long as the labeling is consistent throughout the problem (e.g. the left side should always be 1 and the right side should always be 0, or the left side should always be 0 and the right side should always be 1).

- Add the probabilities of the two symbols to get the probability of the new subtree.

- Remove the symbols from the list and add the subtree to the list.

- Go back through the list and take the two symbols/subtrees with the smallest probabilities and combine those into a new subtree. Remove the original symbols/subtrees from the list, and add the new subtree to the list.

-Repeat until all of the elements are combined.
#######################################################################################
# Time Complexity-
The time complexity analysis of Huffman Coding is as follows-

extractMin( ) is called 2 x (n-1) times if there are n nodes.
As extractMin( ) calls minHeapify( ), it takes O(logn) time.
 
Thus, Overall time complexity of Huffman Coding becomes O(nlogn).

Here, n is the number of unique characters in the given text.

#########################################################################################
Huffman coding is optimal for encoding single characters, but for encoding multiple characters with one encoding, other compression methods are better. Moreover, it is optimal when each input symbol is a known independent and identically distributed random variable having a probability that is the inverse of a power of two.

# NOTE - The file path used in the code is with respect to my system.
