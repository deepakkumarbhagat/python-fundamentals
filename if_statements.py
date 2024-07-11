def average_grade(grade1, grade2):
    ''' (float, float) -> float

    Print average of all passing grade. Print 0.0 if no passing grade
    Print average of both the grades grade1 and grade2 if both are >= 50
    Print exact grade if one of grade1 or grade2 is >= 50.
    
    >>> average_grade(50.0, 50.0)
    50.0
    >> average_grade(100.0, 0.0)
    100.0
    >> average_grade(10.0, 10.0)
    0.0
    '''
    
    total = 0
    grade_count = 0

    if grade1 >= 50:
        total = total + grade1
        grade_count = grade_count + 1
    if grade2 >= 50:
        total = total + grade2
        grade_count = grade_count + 1

    if grade_count > 0:
        print(total / grade_count)
    else:
        print(0.0)

def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> str

    Return the flight status (on time, early, delayed) for a flight that
    was scheduled to arrive at scheduled_time, but is now estimated to arrive
    at estimated_time

    Pre-condition: 0.0 <= scheduled_time < 24.0 and
    0.0 <= expected_time < 24.0 

    >>> report_status(14.3, 14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'

