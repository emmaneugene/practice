# Problem: https://leetcode.com/problems/encode-and-decode-strings

# Time complexity: O(n)
# Space complexity: O(n)
# Use an escape character. But take note to handle the escape character itself during
# serialization and deserialization


class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        newStrs: list[str] = []
        for s in strs:
            res = ""
            for ch in s:
                if ch == "\\":
                    res += "\\"
                res += ch
            newStrs.append(res)
            res = ""

        return "\\n".join(newStrs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res: list[str] = []
        curr = ""
        escape = False

        for ch in s:
            if escape:
                if ch == "n":
                    res.append(curr)
                    curr = ""
                elif ch == "\\":
                    curr += "\\"
                else:
                    print(f"Invalid escape sequence found: \\{ch}")
                escape = False
            else:
                if ch == "\\":
                    escape = True
                    continue

                curr += ch

        res.append(curr)
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


def main():
    codec = Codec()
    print(codec.decode(codec.encode([""])))
    print(codec.decode(codec.encode(["hello"])))
    print(codec.decode(codec.encode(["hello", "World"])))
    print(codec.decode(codec.encode(["he\llo"])))
    print(codec.decode(codec.encode(["he\llo, world", "#1"])))


if __name__ == "__main__":
    main()
