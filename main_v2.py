import itertools

def deduce(ans, **opt):
    assert(opt[ans])

for answer in itertools.product(['A', 'B', 'C', 'D'], repeat=10):
    occur = [0,0,0,0]
    for i in range(10):
        occur[ord(answer[i])-ord('A')] += 1

    try:
        deduce(
            answer[1], 
            A = answer[4] == 'C',
            B = answer[4] == 'D',
            C = answer[4] == 'A',
            D = answer[4] == 'B'
        )
    
        deduce(
            answer[2],
            A = answer[2] not in [answer[5], answer[1], answer[3]],
            B = answer[5] not in [answer[2], answer[1], answer[3]],
            C = answer[1] not in [answer[2], answer[5], answer[3]],
            D = answer[3] not in [answer[2], answer[1], answer[5]]
        )
    
        deduce(
            answer[3],
            A = answer[0] == answer[4],
            B = answer[1] == answer[6],
            C = answer[0] == answer[8],
            D = answer[5] == answer[9]
        )
        
        deduce(
            answer[4],
            A = answer[4] == answer[7],
            B = answer[4] == answer[3],
            C = answer[4] == answer[8],
            D = answer[4] == answer[6]
        )

        deduce(
            answer[5],
            A = answer[7]==answer[1] and answer[7]==answer[3],
            B = answer[7]==answer[0] and answer[7]==answer[5],
            C = answer[7]==answer[2] and answer[7]==answer[9],
            D = answer[7]==answer[4] and answer[7]==answer[8]
        )

        deduce(
            answer[6],
            A = occur[ord('C')-ord('A')] == min(occur),
            B = occur[ord('B')-ord('A')] == min(occur),
            C = occur[ord('A')-ord('A')] == min(occur),
            D = occur[ord('D')-ord('A')] == min(occur),
        )

        deduce(
            answer[7],
            A = abs(ord(answer[6]) - ord(answer[0])) != 1,
            B = abs(ord(answer[4]) - ord(answer[0])) != 1,
            C = abs(ord(answer[1]) - ord(answer[0])) != 1,
            D = abs(ord(answer[9]) - ord(answer[0])) != 1,
        )

        deduce(
            answer[8],
            A = (answer[0]==answer[5])^(answer[5]==answer[4]),
            B = (answer[0]==answer[5])^(answer[9]==answer[4]),
            C = (answer[0]==answer[5])^(answer[1]==answer[4]),
            D = (answer[0]==answer[5])^(answer[8]==answer[4]),
        )

        deduce(
            answer[9],
            A = max(occur)-min(occur) == 3,
            B = max(occur)-min(occur) == 2,
            C = max(occur)-min(occur) == 4,
            D = max(occur)-min(occur) == 1,
        )

        print('The answer of this test is:')
        print(answer)

    except AssertionError:
        continue
