import csv
from collections import defaultdict


def gale_shapley(participants_func, teams_func, team_size_func):
    # convert team size to a dictionary
    team_size_func = {team: int(size) for team, size in zip(teams_func, team_size_func)}

    # convert participants preferences to a dictionary
    participants_preferences = defaultdict(dict)
    for participant_func, preferences_func in participants_func.items():
        for rank, team in enumerate(preferences_func):
            participants_preferences[participant_func][team] = rank

    # Initialize dictionaries
    matching = {}
    team_matching = defaultdict(list)
    free_participants = list(participants_func.keys())

    # While there are free participants left, fill teams with participants
    while free_participants:
        participant_func = free_participants.pop(0)
        participant_preferences = participants_preferences[participant_func]
        for team in participant_preferences:
            if len(team_matching[team]) < team_size_func[team]:
                matching[participant_func] = team
                team_matching[team].append(participant_func)
                break
            else:
                current_participant = team_matching[team][-1]
                if participant_preferences[team] < participants_preferences[current_participant][team]:
                    matching[participant_func] = team
                    team_matching[team].append(participant_func)
                    free_participants.append(current_participant)
                    break

    return matching


def validate_csv_data(teams, team_sizes, participants):
    # Check if the number of teams matches the number of team sizes
    if len(teams) != len(team_sizes):
        raise ValueError("The number of teams does not match the number of team sizes.")

    # Check if each participant has the correct number of preferences
    for participant, preferences in participants.items():
        if len(preferences) != len(teams):
            raise ValueError(f"Participant {participant} does not have the correct number of preferences.")

    # Check if team sizes are positive integers
    if any(size <= 0 for size in team_sizes):
        raise ValueError("Team sizes must be positive integers.")

    # Check if preferences are valid team indices
    for participant, preferences in participants.items():
        for preference in preferences:
            if not preference.isdigit() or int(preference) < 1 or int(preference) > len(teams):
                raise ValueError(f"Invalid preference {preference} for participant {participant}.")

    # Check if each participant has unique preferences
    for participant, preferences in participants.items():
        if len(preferences) != len(set(preferences)):
            raise ValueError(f"Participant {participant} has duplicate preferences.")


def main():
    # Read preferences from the csv file
    with open('preferences.csv', newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        # Store teams and remove null column
        teams = next(reader)
        teams.pop(0)

        # Store team sizes, remove row name and convert to integers
        team_sizes = next(reader)
        team_sizes.pop(0)
        team_sizes = [int(size) for size in team_sizes]

        # Store participants and preferences
        participants = {row[0]: row[1:] for row in reader}
        # Rework participant: replace preference number with team name
        participants_strings = {}
        for participant, preferences in participants.items():
            participants_strings[participant] = ['' for _ in range(len(team_sizes))]
            for rank, team in enumerate(preferences):
                participants_strings[participant][int(team) - 1] = teams[rank]

    # Validate the CSV data
    validate_csv_data(teams, team_sizes, participants)

    # Perform the Gale-Shapley algorithm
    matching = gale_shapley(participants_strings, teams, team_sizes)

    # Print the matching nicely
    for team_name in teams:
        print(team_name, ': ', end='')
        for participant, team in matching.items():
            if team == team_name:
                print(participant, end=', ')
        print()


if __name__ == '__main__':
    main()
