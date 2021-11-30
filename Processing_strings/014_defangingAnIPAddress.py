class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""
        for i in address:
            if i == ".":
                new_address += "[.]"
            else:
                new_address += i
        return new_address


if __name__ == '__main__':
    address = "1.1.1.1"
    print(Solution().defangIPaddr(address))
