def string_input() -> list:
    print('Входные данные:')
    blocks_amount = int(input())  # blocks amount
    _space = input()  # space
    blocks = []

    for _block in range(blocks_amount):
        n = int(input())  # candidates amount
        candidates = []  # for candidates names
        candidates_votes = {}  # votes from first order in form candidate: {votes, index}

        for i in range(n):  # candidates enter
            candidate = input()
            candidates.append(candidate)
            candidates_votes[candidate] = {
                'votes': 0,
                'index': i
            }

        people_votes = []

        while True:
            vote = input()
            if vote == '':  # on blank line - stop entering
                break

            vote = [int(i) - 1 for i in vote.split(' ')]
            people_votes.append(vote)

            candidates_votes[candidates[vote[0]]] = {
                'votes': candidates_votes[candidates[vote[0]]]['votes'] + 1,
                'index': vote[0]
            }

        blocks.append((people_votes, candidates_votes))

    return blocks


def remove_lowest_candidates():
    pass


def get_new_people_vote():
    pass


def
