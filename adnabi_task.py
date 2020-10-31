"""
    Adnabi interview task

    author: Satish Kumar

    assumption : list of quiz participants is sorted by days
"""
import sys
from collections import Counter

test_case = [
['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam'],
] 


def get_participants_every_day(list_of_participants):
    '''
        i/p: list of lists of participants
        o/p: list of particpants who have attended every day, 
        returns empty array on passing empty array
    '''
    every_day_participants = list()

    try:
        counts = get_as_counter(list_of_participants)
        for participant, attend_count in counts.items():
            if attend_count == len(list_of_participants):  # when count = number of days quiz was held
                every_day_participants.append(participant)
    except (KeyError, IndexError, TypeError) as e:
        # catching basic errors and skipping, i.e returns empty
        print(e)
        pass

    return sorted(every_day_participants)


def get_particants_one_time(list_of_participants):
    '''
        i/p: list of lists of participants
        o/p: participants who had attended only once , 
        returns empty array on passing empty array
    '''
    one_time_participants = list()

    try:
        counts = get_as_counter(list_of_participants)
        for participant, attend_count in counts.items():
            if attend_count == 1:
                one_time_participants.append(participant)
    except (KeyError, IndexError, TypeError) as e:
        # catching basic errors and skipping, i.e returns empty
        print(e)
        pass

    return sorted(one_time_participants)


def get_participants_first_day_one_time(list_of_participants):
    '''
        i/p: list of participants
        o/p: participants who have attended one time only on the first day, 
        returns empty on passing empty array
    '''
    first_day_one_time_participants = list()
    try:
        first_day_participants = list_of_participants[0]
    except KeyError:
        first_day_participants = []

    try:
        counts = get_as_counter(list_of_participants)
        for participant, attend_count in counts.items():
            if attend_count == 1 and participant in first_day_participants:
                first_day_one_time_participants.append(participant)
    except (KeyError, IndexError, TypeError) as e:
        # catching basic errors and skipping, i.e returns empty
        print(e)
        pass

    return sorted(first_day_one_time_participants)


def get_as_counter(list_of_participants):
    '''
        i/p: list of lists 
        o/p: counter object with participant as key and quiz attendance as value
    '''
    overall_counts = Counter()

    for entry in list_of_participants:
        overall_counts = overall_counts + Counter(entry)

    return overall_counts


if __name__ == "__main__":

    print(get_participants_every_day(test_case))
    print(get_particants_one_time(test_case))
    print(get_participants_first_day_one_time(test_case))
