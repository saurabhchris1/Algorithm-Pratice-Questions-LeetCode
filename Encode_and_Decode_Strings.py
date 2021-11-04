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