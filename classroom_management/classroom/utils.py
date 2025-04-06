def calculate_performance(student):
    assessments = student.assessments.order_by("date")
    if not assessments.exists():
        return 0.0, "Stable"

    scores = [a.score for a in assessments]
    average = sum(scores) / len(scores)

    # Determine performance trend (simple logic)
    if len(scores) >= 3:
        if scores[-1] > scores[-2] > scores[-3]:
            status = "Progressing"
        elif scores[-1] < scores[-2] < scores[-3]:
            status = "Declining"
        else:
            status = "Stable"
    else:
        status = "Stable"

    return round(average, 2), status
