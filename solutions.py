def solution(R):
    maximum_indicator = 0
    pothole_count = 0
    pothole_depth = 0

    for segment_depth in R:
        if segment_depth == 0:
            maximum_indicator = max(maximum_indicator, pothole_count * pothole_depth)
            pothole_count = 0
            pothole_depth = 0
        else:
            pothole_count += 1
            pothole_depth = max(pothole_depth, segment_depth)

    maximum_indicator = max(maximum_indicator, pothole_count * pothole_depth)
    return maximum_indicator

print(solution([1, 3, 1, 4, 5]))
