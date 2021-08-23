A,B,C = gets().chomp.split(' ').map { |n| n.to_i }
exit if !( 1 <= A && A <= 100 && 1 <= B && B <= 100 && 0 <= C && C < B)

if A % 2 == 0 && B % 2 == 0 && C % 2 == 1 
    puts 'NO'
    exit
end
for I in (1..10**5) do #繰り返しはBの回数まででOKなのでこんなにやる必要はない。。。
    if (( A * I ) % B ) == C
        puts 'YES'
        exit
    end
end
puts 'NO'
