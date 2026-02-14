def task1_4():
    blocks = int(input())  # blocks amount
    blocks_results = []

    for _block in range(blocks):
        _space = input()  # space
        n = int(input())  # candidates amount
        candidates = []   # for candidates names

        for i in range(n):  # candidates enter
            candidate = input()
            candidates.append(candidate)

        people_amount = 0
        people_votes = []
        candidate_votes_dict = {}  # votes from first order in form candidate: {votes, index}
        candidate_votes = []  # votes from first order in form [id, candidate, votes]

        while True:
            vote = input()
            if vote == '':  # on blank line - stop entering
                break

            people_amount += 1

            vote = [int(i) - 1 for i in vote.split(' ')]
            people_votes.append(vote)

            candidate_votes_dict[candidates[vote[0]]] = {
                'votes': candidate_votes_dict.get(candidates[vote[0]], {}).get('votes', 0) + 1,
                'index': vote[0]
            }

        for candidate, info in candidate_votes_dict.items():
            candidate_votes.append(
                {
                    'index': info['index'],
                    'candidate': candidate,
                    'votes': info['votes']
                }
            )

        print(calculate_votes(people_votes, candidate_votes, people_amount))


def calculate_votes(people_votes: list, candidate_votes: list, people_amount: int):
    candidate_votes = list(sorted(candidate_votes, key=lambda candidate_vote: candidate_vote['votes'], reverse=True))  # sort from high to low amount of votes

    if all(candidate_vote['votes'] == candidate_votes[0]['votes'] for candidate_vote in candidate_votes):  # if every votes amount equals
        return [candidate_vote['candidate'] for candidate_vote in candidate_votes]
    elif candidate_votes[0]['votes'] / people_amount >= 0.5:  # if biggest amount of votes higher or equals to 50%
        return [candidate_votes[0]['candidate']]
    else:
        candidate_votes.reverse()  # reversed for faster finding candidates with lower votes
        candidate_votes_cut = candidate_votes.copy()  # copying array
        candidate_votes_removed = []  # array for candidates who was removed due to the lowest votes
        candidate_votes_removed_indexes = []  # array for indexes of candidates from previous array
        for i in range(len(candidate_votes)):
            if candidate_votes[i]['votes'] == candidate_votes[0]['votes']:  # if candidate votes equals to minimum candidate votes
                candidate_votes_removed.append(candidate_votes[i])  # add candidate to array
                candidate_votes_removed_indexes.append(candidate_votes[i]['index'])  # add candidate index to array
                del candidate_votes_cut[i]  # delete candidate from copied original array
            else:
                break

        for i in range(len(candidate_votes_removed)):
            index_removed = candidate_votes_removed[i]['index']  # index of candidate who was removed
            for k in range(len(people_votes)):
                people_vote = people_votes[k]
                if people_vote[0] == index_removed:
                    new_people_vote = []
                    for j in range(len(people_vote[1:])):
                        current_people_vote = people_vote[1:][j]
                        if current_people_vote in candidate_votes_removed_indexes:
                            continue

                        new_people_vote = people_vote[(1 + j):]
                        for candidate_vote in candidate_votes:
                            if candidate_vote['index'] == current_people_vote:
                                candidate_vote['votes'] = candidate_vote.get('votes', 0) + 1
                        break
                    people_votes[k] = new_people_vote

        result = calculate_votes(people_votes, candidate_votes_cut, people_amount)

        return result


if __name__ == '__main__':
    task1_4()
