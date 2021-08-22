N,M = gets().chomp.split(' ').map { |n| n.to_i }
students = [nil] * N
checkpoints = [nil] * M
(0..N-1).each { |n|
  students[n] = gets().chomp.split(' ').map { |n| n.to_i }
}
(0..M-1).each { |m|
  checkpoints[m] = gets().chomp.split(' ').map { |m| m.to_i }
}

exit if N < 0 || N > 50 || M < 0 || M > 50

students.each { |student| exit if student[0] < -100000000 || student[1] > 100000000}
checkpoints.each { |checkpoint| exit if checkpoint[0] < -100000000 || checkpoint[1] > 100000000}

distance = [40000000000000000] * N
result = [0] * N
count = 0

students.each { |student|
    checkpoint_count = 0
    checkpoints.each { |checkpoint|
        tmp_distance = (student[0] - checkpoint[0]).abs + (student[1] - checkpoint[1]).abs
        if distance[count] > tmp_distance
            distance[count] = tmp_distance
            result[count] = checkpoint_count + 1
        end
        checkpoint_count += 1
    }
    count += 1
}
result.each { |i| puts i }