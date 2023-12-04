class NumberRotations
    def initialize(n)
        @upper_limit = n
        @sum_of_rotations = get_five_sum(@upper_limit)
    end

    def get_five_sum(n)
        sum = 0
        for i in 11..n.to_i do
            rotation = get_rotation(i)
            if is_divisible(i, rotation) then
                sum = sum + i
            end
        end
        return sum.to_s[-5..-1]
    end
    
    def get_rotation(n)
        r = n % 10
        m = (n / 10).floor
        return (m + (r * (10 ** m))).floor
    end
    
    def is_divisible(n, rotation)
        return rotation % n == 0
    end

    def to_s()
        to_str
    end

    def to_str()
        @sum_of_rotations
    end
end

nr = NumberRotations.new(ARGV[0])
puts nr.to_s