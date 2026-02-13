def task1_4():
    blocks = int(input())  # blocks amount
    blocks_results = []

    for block in range(blocks):
        _space = input()  # space
        n = int(input())  # candidates amount
        candidates = []   # for candidates names

        for i in range(n):  # candidates enter
            candidate = input()
            candidates.append(candidate)

        votes_amount = 0
        votes = []
        votes_statistics_rounds = [ {} for _ in range(n) ]  # vote results by order, stats after first, second, etc.
        votes_statistics_rounds_percentage = [ {} for _ in range(n) ]
        while True:
            vote = input()
            if vote == '':  # on blank line - stop entering
                break

            vote = [int(i) for i in vote.split(' ')]
            votes.append(vote)

            votes_amount += 1
            for i in range(n):
                people_vote = vote[i]
                votes_statistics_rounds[i][candidates[people_vote - 1]] = votes_statistics_rounds[i].get(candidates[people_vote - 1], 0) + 1  # add vote to candidate
                votes_statistics_rounds_percentage[i][candidates[people_vote - 1]] = votes_statistics_rounds[i][candidates[people_vote - 1]] / votes_amount

        votes_final_statistics = {}
        votes_final_statistics_percentage = {}
        for vote_round in range(n):
            votes_statistics_rounds_percentage[vote_round] = dict(sorted(votes_statistics_rounds_percentage[vote_round].items(), key=lambda k: k[1], reverse=True))

            votes_min = ['', votes_amount]
            for key, value in votes_statistics_rounds_percentage[vote_round].items():
                if value >= 0.5:
                    blocks_results.append([key])
                if value <= votes_min[1]:
                    votes_min[0] = key
                    votes_min[1] = value

            for vote in votes:
                if vote[vote_round]


def calculate_votes(current_round: dict, second_round: dict, votes_amount: int, votes: list):
    votes_min = ['', votes_amount]
    for key, value in current_round.items():
        if value / votes_amount >= 0.5:
            return [key]
        if value <= votes_min[1]:
            votes_min[0] = key
            votes_min[1] = value


if __name__ == '__main__':
    task1_4()
