partyA = set(["Park", "Kim", "Lee"])  # partyA = {"Park", "Kim", "Lee"}
partyB = set(["Park", "Choi"])  # partyB = {"Park", "Choi"}


def SequenceToString(Sequence):
    result = ""
    for i in Sequence:
        result += i + ", "
    return result+"\b\b"


print("파티 A, B에 참석한 사람들 :", SequenceToString(partyA.union(partyB)))
print("파티 A, B 중복없이 참석한 사람 :", SequenceToString(partyA.symmetric_difference(partyB)))
print("파티 A에만 참석한 사람 :", SequenceToString(partyA.difference(partyB)))
