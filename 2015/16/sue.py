class Sue:

    def __init__(self, line):
        self.details = {}
        s = self.lineSplitter(line)
        self.number = s[0]
        self.details[s[1]] = int(s[2])
        self.details[s[3]] = int(s[4])
        self.details[s[5]] = int(s[6])

    def lineSplitter(self, line):
        parts = line.split(" ")
        return (parts[1][0:-1],parts[2][0:-1],parts[3][0:-1],parts[4][0:-1],parts[5][0:-1],parts[6][0:-1],parts[7])

