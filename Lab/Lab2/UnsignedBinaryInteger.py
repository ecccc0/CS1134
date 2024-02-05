class UnsignedBinaryInteger:
    def __init__(self, num_str):
        self.num_str = num_str
    def __lt__(self, other):
        if self.num_str == other.num_str or len(self.num_str) > len(self.num_str):
            return False
        if len(self.num_str) < len(other.num_str):
            return True
        else:
            for i in range(len(self.num_str)):
                if int(self.num_str[i]) > int(other.num_str[i]):
                    return False
            return True
    def __gt__(self, other):
        if self.num_str == other.num_str or len(self.num_str) < len(self.num_str):
            return False
        if len(self.num_str) > len(other.num_str):
            return True
        else:
            for i in range(len(self.num_str)):
                if int(self.num_str[i]) < int(other.num_str[i]):
                    return False
            return True
    def __eq__(self, other):
        return self.num_str == other.num_str
    def is_twos_power(self):
        return (self.num_str[0] == '1' and not '1' in self.num_str[1:]) or (self.num_str == "0")
    def largest_twos_power(self):
        return "1" + "0" * (len(self.num_str) - 1) if len(self.num_str) > 1 else "0"
    def __repr__(self):
        return "0b" + self.num_str