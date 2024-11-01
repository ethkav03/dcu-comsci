class ReversibleNumbers
    class ReversibleNumber
        def initialize(n)
            @number = n
            @reverse_number = reverse(n)
            @sum = @number + @reverse_number
            @is_reversible = reversible(@number, @reverse_number)
        end

        def is_reversible()
            return @is_reversible
        end

        def reversible(n, reverse_n)
            if all_odd(n + reverse_n) then
                return true
            end
            return false
        end

        def reverse(n)
            s = n.to_s
            reversed = s.reverse()
            return reversed.to_i
        end
    
        def all_odd(n)
            while n > 0 do
                x = n % 10
                if x % 2 == 0 then
                    return false
                end
                n = (n / 10).floor
            end
            return true
        end
    end

    def initialize(upperLimit)
        @upperLimit = upperLimit.to_i
        @reversible_numbers_count = get_reversible_numbers(@upperLimit)
    end

    def get_reversible_numbers(n)
        total = 0
        for i in 1..n-1 do
            rn = ReversibleNumber.new(i)
            if rn.is_reversible then
                total += 1
            end
        end
        return total
    end

    def to_s()
        @reversible_numbers_count
    end
    
    def to_str()
        to_s
    end
end

r = ReversibleNumbers.new(ARGV[0])
puts r.to_s