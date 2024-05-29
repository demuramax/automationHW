# There are lists of testers (names or ids) who:
# - can write test designs
# - can write test scripts
# - can review scripts
# - out of work today (here could be only testers from 3 previous groups)
# Any tester can be listed in one or more groups.
# Create the following sorted lists:
# - all testers in the team
# - testers who can only write scripts
# - testers who are at work today
# - testers who could write and review scripts, and are at work today
# The results should be sorted.

# Example:
test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

# all testers in the team
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# testers who can only write scripts
# [4, 6, 7, 8]
#
# testers who are at work today
# [3, 4, 7, 8, 9, 10]
#
# testers who could write and review scripts, and are at work today
# [3]

# test_design_writers.extend(test_scripters)
# print(test_design_writers)

all_testers = []
all_testers.extend(test_design_writers)
all_testers.extend(test_scripters)
all_testers.extend(reviewers)

all_testers = set(all_testers)
print(f'all testers in the team: {all_testers}')

test_scripters = set(test_scripters)
test_design_writers = set(test_design_writers)
reviewers = set(reviewers)
out_of_office_today = set(out_of_office_today)

testers_only_scripters = list(all_testers.difference(test_design_writers.union(reviewers)))
testers_only_scripters.sort()
print(f'testers_only_scripters: ®{testers_only_scripters}')

testers_at_work_today = all_testers.difference(out_of_office_today)
print(f'testers_at_work_today: {testers_at_work_today}')

testers_write_review_scripts_today = (test_design_writers.intersection(test_scripters)).difference(out_of_office_today)
print(f'testers_write_review_scripts_today: {testers_write_review_scripts_today}')
