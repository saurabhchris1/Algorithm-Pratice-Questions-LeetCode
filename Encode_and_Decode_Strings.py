# Design an algorithm to encode a list of strings to a string. The encoded string is then
# sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# You are not allowed to solve the problem using any serialize methods (such as eval).
#
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2
#
# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
#
# Input: dummy_input = [""]
# Output: [""]


class Codec:
  def encode(self, strs: [str]) -> str:
    res = []

    for x in strs:
      res.append(self.len_to_str(x) + x)

    print(res)

    return "".join(res)

  def len_to_str(self, x):

    res = []
    x = len(x)
    for i in range(4):
      bits = x >> (i * 8) & 0xff
      res.append(chr(bits))

    res.reverse()
    return "".join(res)

  def str_to_len(self, byte_str):

    result = 0
    for ch in byte_str:
      result = result * 256 + ord(ch)
    return result

  def decode(self, s: str) -> [str]:
    """Decodes a single string to a list of strings.
    """
    i, n = 0, len(s)
    output = []

    while i < n:
      length = self.str_to_len(s[i:i + 4])
      i += 4
      output.append(s[i: i + length])
      i += length

    return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# Understanding bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
#
# all you need to do is encode the length of x into 4 bytes ( why 4 bytes - integer size - 4 bytes = [8bits, 8bits, 8bits, 8bits])
#
# ok so how do you get a X(length of str) total size into chunks of 8 bits ?
# 2.1 >> is right shift - which means if you have 101111 >> 2 - this right shift moves 101111, 2 times to the right - which
# becomes 1011
# 2.2 if you go to python terminal and type 0xff you get 8 1's which represents 11111111 = a BYTE
# 2.3 if you AND(&) any number with 0xff = it gives you the right most 8 bits of the number
# example: 1. bin(291) (binary of 291) is '0b100100011'
# 2. oxff binary is '0b11111111'
# 3. now if you 291 & 0xff = you get last 8 bits of 291 == 00100011
# If you understand this - you understood the solution.
#
# Now as explained in the 2 point. The python solution line 6 we take the whole length of the string (len(str)) - we have to
# encode that into [8bits, 8 bits, 8bits, 8bits]
# example: 1. lets say our total length is 291 ( in binary its bin(291) = '0b100100011')
# 2. what you have to do now ? we grab the right most 8 bits - how do you grab right most 8 bits ?
# 2.1 as mentioned above you do 291 & 0xff = you get last 8 bits
#
# Now you already have right most 8 bits - in next iteration you are interested in NEXT 8 bits - how do you get
# that ? we move 291 >> 8 ( which removes the last 8 bits we already computed) - which means if you do
# (291 >> 8 ) & 0xff = it gives you the next right most 8 bits
#
# as already mentioned we need 4 chunks of 8 bits [8bits, 8bits, 8bits, 8bits]
# 4.1 [ for i in range(4)] thats why the range is 4 ( 0, 1, 2, 3)
#
# Once you compute all the 8bits we need to convert to char hence its [chr((x >> (i * 8)) & 0xff) for i in range(4)]