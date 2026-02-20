def task1_4() -> None:
    """
    Function to calculate Australian voting
    :return: None
    """
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for block in blocks:
        people, votes = block
        result = calculate_votes(people, votes)

        for candidate in result:
            print(candidate)
        print()


def blocks_input() -> list:
    """
    Function to enter input blocks
    :return: List with blocks
    """
    blocks_amount = int(input())  # blocks amount
    _space = input()  # space
    blocks = []

    for _block in range(blocks_amount):
        n = int(input())  # candidates amount
        candidates = []  # for candidates names
        votes = {}  # votes from first order in form candidate: {votes, index}

        for i in range(n):  # candidates enter
            candidate = input()
            candidates.append(candidate)
            votes[candidate] = {
                'votes': 0,
                'index': i
            }

        people = []

        while True:
            vote = input()
            if vote == '':  # on blank line - stop entering
                break

            vote = [int(i) - 1 for i in vote.split(' ')]
            people.append(vote)

            votes[candidates[vote[0]]] = {
                'votes': votes[candidates[vote[0]]]['votes'] + 1,
                'index': vote[0]
            }

        blocks.append((people, votes))

    return blocks


def get_lowest_candidate(votes: dict) -> tuple[str, dict]:
    """
    Get candidate from dictionary with the lowest votes
    :param votes: Dictionary with candidates and their votes and indexes
    :return: A tuple with candidate name and his votes and index
    """
    lowest_vote = next(iter(votes.values()))
    lowest = None

    for candidate, vote in votes.items():
        if vote['votes'] <= lowest_vote['votes']:
            lowest_vote = vote
            lowest = (candidate, vote)

    return lowest


def get_highest_candidate(votes: dict) -> tuple[str, dict]:
    """
    Get candidate from dictionary with the highest votes
    :param votes: Dictionary with candidates and their votes and indexes
    :return: A tuple with candidate name and his votes and index
    """
    highest_vote = next(iter(votes.values()))
    highest = None

    for candidate, vote in votes.items():
        if vote['votes'] >= highest_vote['votes']:
            highest_vote = vote
            highest = (candidate, vote)

    return highest


def remove_lowest_candidates(votes: dict) -> tuple[dict, dict]:
    """
    Form two new dictionaries with candidates and their votes and indexes without the lowest ones and dictionary with
    the lowest candidates, their votes and indexes
    :param votes: Dictionary with candidates and their votes and indexes
    :return:
    """
    lowest_candidate, lowest_vote = get_lowest_candidate(votes)

    new_votes = {}
    removed_votes = {}

    for candidate, vote in votes.items():
        if vote['votes'] == lowest_vote['votes']:
            removed_votes[candidate] = vote
        else:
            new_votes[candidate] = vote

    return new_votes, removed_votes


def get_new_person_vote(votes: dict, person: list) -> tuple[dict, list]:
    """
    Get new vote index for existing candidate from person votes order
    :param votes: Dictionary with candidates and their votes and indexes
    :param person: List with person votes order
    :return: Tuple with dictionary that contains updated votes and new list of person votes order
    """
    new_person = []

    for i in range(1, len(person)):
        index = person[i]

        for candidate, vote in votes.items():
            if vote['index'] == index:
                vote['votes'] += 1
                new_person = person[i:]

                return votes, new_person

    return votes, new_person


def check_votes_equal(votes: dict) -> list:
    """
    Check if every candidate vote in list equal
    :param votes: Dictionary with candidates and their votes and indexes
    :return: Empty list if candidates votes not equal and list with candidates names if they are equal
    """
    lowest_candidate, lowest_vote = get_lowest_candidate(votes)

    result = []

    for candidate, vote in votes.items():
        if vote['votes'] != lowest_vote['votes']:
            return []

        result.append(candidate)

    return result


def calculate_votes(people: list, votes: dict) -> list:
    """
    Recursive votes calculation for voting
    :param people: List with every person votes order
    :param votes: Dictionary with candidates and their votes and indexes
    :return: List of candidates who win voting
    """
    votes_equal = check_votes_equal(votes)
    highest_candidate, highest_vote = get_highest_candidate(votes)

    if votes_equal:
        return votes_equal
    elif highest_vote['votes'] / len(people) >= 0.5:
        return [highest_candidate]
    else:
        new_votes, removed_votes = remove_lowest_candidates(votes)

        for candidate, vote in removed_votes.items():
            for person in people:
                if person[0] == vote['index']:
                    new_votes, person = get_new_person_vote(new_votes, person)

                    break

        result = calculate_votes(people, new_votes)

        return result


if __name__ == '__main__':
    task1_4()
