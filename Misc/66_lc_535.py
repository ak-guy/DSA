'''
535. Encode and Decode TinyURL
'''
import string, random

class Codec:
    _mappings = {}
    _base_url = 'http://tinyurl.com/'
    _range = string.ascii_lowercase + string.ascii_uppercase + string.digits
    _tiny_url_length = 8 # total urls combination possible 2.18e+14 or 218340105584896

    def encode(self, longUrl: str) -> str:
        """ Encodes a URL to a shortened URL """
        sub_url = ''.join(random.choices(Codec._range, k=Codec._tiny_url_length))
        tiny_url = Codec._base_url + sub_url
        Codec._mappings.update({tiny_url: longUrl})
        
        return tiny_url

    def decode(self, shortUrl: str) -> str:
        """ Decodes a shortened URL to its original URL """
        return Codec._mappings.get(shortUrl, None)

# Your Codec object will be instantiated and called as such:
url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
print(codec.decode(codec.encode(url)))
