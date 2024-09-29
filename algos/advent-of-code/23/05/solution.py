import sys
import bisect

# Conversion is a process of taking inputs -> outputs continuously for each ruleset
# specified within the input file

# TODO: Optimize
# Parse rules into a set of ranges


class ruleSet:
    def __init__(self, lines: list[str]) -> None:
        vals = [list(map(lambda x: int(x), l.split())) for l in lines]
        rules = []

        for v in vals:
            start: int = v[1]
            end: int = v[1] + v[2] - 1
            diff: int = v[0] - v[1]
            rules.append((start, end, diff))

        rules.sort(key=lambda x: x[0])

        self.rules = rules

    def convert(self, val: int) -> int:
        idx = bisect.bisect_left(self.rules, val, key=lambda x: x[1])
        if idx < len(self.rules) and self.rules[idx][0] <= val:
            return val + self.rules[idx][2]
        return val


def getMinLocationVal(seeds: list[int], rules: list[ruleSet]) -> int:
    locations = []
    for s in seeds:
        toConvert = s
        for r in ruleSets:
            toConvert = r.convert(toConvert)
        locations.append(toConvert)

    return min(locations)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    seedVals = list(map(lambda x: int(x), lines.pop(0).split(":")[1].split()))

    seedRanges = [
        [seedVals[i], seedVals[i] + seedVals[i + 1]] for i in range(0, len(seedVals), 2)
    ]

    ruleSets: list[ruleSet] = []
    currRules: list[str] = []
    foundRules = False

    for l in lines:
        if l == "\n":
            continue
        if "map" in l:
            if foundRules:
                ruleSets.append(ruleSet(currRules))
            foundRules = True
            currRules = []
        else:
            currRules.append(l)

    ruleSets.append(ruleSet(currRules))

    ans1: int = getMinLocationVal(seedVals, ruleSets)

    minsFromRanges = []
    for sr in seedRanges:
        minsFromRanges.append(getMinLocationVal(list(range(sr[0], sr[1])), ruleSets))

    print(f"Part 1: {ans1}\nPart 2: {min(minsFromRanges)}")
