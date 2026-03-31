class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}#{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        count = ""
        words = list(s)
        word = ''
        output = []

        while True:
            if i == len(words):
                return output
            while words[i] != "#":
                count += words[i]
                i += 1
            i += 1
            count = int(count)
            while count > 0:
                word += words[i]
                i += 1
                count -= 1
            output.append(word)
            word = ""
            count = ""





